#pragma once

//////////////////////////////////////////////////
// BIBLIOTECAS ///////////////////////////////////
//////////////////////////////////////////////////

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <math.h>
#include <wiringPi.h>
#include <iostream>
#include <bcm2835.h>
#include "DigiPotX9Cxxx-vRPi.h"
#include "LambertW.h"

//////////////////////////////////////////////////
// CONSTANTES ////////////////////////////////////
//////////////////////////////////////////////////

const double RES_MIN = 37.661;
const double RES_MAX = 9402.4;
const double LEVELS = 100.0;

const uint8_t LVL_MIN = 0;
const uint8_t LVL_MAX = 99;

const double QUANT_RES = (RES_MAX - RES_MIN) / (LEVELS - 1.0);

const uint8_t starti = 0x01;
const uint8_t endi = 0x00;

//////////////////////////////////////////////////
// MACROS ////////////////////////////////////////
//////////////////////////////////////////////////

//#define INCPIN	0
//#define UDPIN	1
//#define CSPIN	4

#define INCPIN	0
#define UDPIN	1
#define CSPIN	4


#define SIGMOID_M(v,a_minus,d_minus) 1.0 / (1.0 + exp(-a_minus * (v + d_minus)))
#define SIGMOID_P(v,a_plus,d_plus) 1.0 / (1.0 + exp(-a_plus * (v - d_plus)))
#define LAMBDA(v,old,a_minus,a_plus,d_minus,d_plus) fmin(SIGMOID_M(v,a_minus,d_minus), fmax(old, SIGMOID_P(v,a_plus,d_plus)))
#define VOLT_READ() mcp3008_read(0)*v_slope + v_intercept

//////////////////////////////////////////////////
// PROTOTIPOS ////////////////////////////////////
//////////////////////////////////////////////////

int run_mem(void);
int spi_setup(void);
int reset(void);
int inc(uint8_t lvls);
int dec(uint8_t lvls);
int set_resistance(float res);
int mcp3008_read(uint8_t chan);
int mcp3008_data(int frequency, int interval, uint8_t channel);
void modelo_hp(double, double, int);
void modelo_hdp(double, double, float, float, float, float, int);

//////////////////////////////////////////////////
// FUNCIONES GENERALES ///////////////////////////
//////////////////////////////////////////////////

int run_mem(void) {

	wiringPiSetup();

	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	//emu01->reset();
	emu01->increase(DIGIPOT_MAX_AMOUNT);


	for (int k = 0; k<100; k++) {
		emu01->increase(1);
		delay(200);
		std::cout << k << "\n";
	}

	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

/*	Ec. 2 del informe de labo 6 del 2018.
Observaciones:
* Multiplica por 1.0e-9 para pasar de ns a s.
* mcp3008_read(0) es la lectura de voltaje en bits (entre bornes del memristor).
* v_slope son los volts/bit (antes de ser atenuados).
* v_intercept es (-) el offset (antes de ser atenuado).
* I = V/res = (mcp3008_read(0)*v_slope+v_intercept)/res
*/

void modelo_hp(double w = 0.5, double mu = 1.0, uint8_t lvl_on = 0, uint8_t lvl_off = DIGIPOT_MAX_AMOUNT, int n_meds = 1000) {

	const int8_t lvl_diff = lvl_off-lvl_on;

	const double r_off = RES_MIN + QUANT_RES * lvl_off;
	const double r_on = RES_MIN + QUANT_RES * lvl_on;
	const double r_diff = QUANT_RES * lvl_diff;

	const double v_off = 2.505; // Offset de voltaje
	//const double v_att = 0.6734; // Atenuación de voltaje
	const double v_att = 1;
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;

	double constante = mu*r_on*1.0e-9*v_slope;
	double mcp_correction = v_intercept/v_slope;

	uint8_t r_level = lvl_off - (uint8_t)rint(w*((double)lvl_diff));

	//std::cout << (double)r_level << ' ' << w*((double)lvl_diff) << ' ' << (double)lvl_off << std::endl;

	double R = RES_MIN+r_level*QUANT_RES;

	struct timespec gettime_now;
	float dt, t_prev, t_cur;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->increase(DIGIPOT_MAX_AMOUNT);
	emu01->set(r_level);

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;
	
	// MEDICIÓN DE TIEMPO DE INTEGRACIÓN O w (OPCIONAL)
	int i = 0;
	double* ret_dt = new double[n_meds];
	double * ret_w = new double[n_meds];

	while(1)
	{
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		t_cur = gettime_now.tv_nsec;
		dt = t_cur - t_prev;
		if(dt<0.0) dt += 1.0e+9;

		w += (double)dt*constante*( (double)mcp3008_read(0)+mcp_correction)/R;
		
		if(w<0.0) w = 0.0;
		else if(w>1.0) w = 1.0;

		r_level = lvl_off - (uint8_t)rint(w*((float)lvl_diff));
		
		emu01->set(r_level);
		
		R = RES_MIN+r_level*QUANT_RES;
		
		//emu01->set(uint8_t(rint(((float)(R - RES_MIN)) / ((float)QUANT_RES))));
		
		// MEDICIÓN DE w, tiempo de integración, etc. (DESCOMENTAR EN NECESIDAD)
		//ret_dt[i] = dt;
		//ret_w[i] = w;
		//if(++i>n_meds) break;
	}

	// IMPRESIÓN DE TIEMPOS DE INTEGRACIÓN o w
	//for(int i=0; i<n_meds;i++) std::cout << ret_dt[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_w[i] << "\t";

}

//////////////////////////////////////////////////

// v0 0.3
// vgen 4
// delta 0.2
// t0 0.01
// 15 / 30

void modelo_hdp(double w = 0.5, double a_minus = 1.0, double a_plus = 1.0, double d_minus = 1.0, double d_plus = 1.0, double t0 = 1.0, double v0 = 1.0, uint8_t lvl_on = 0, uint8_t lvl_off = 99, int n_meds = 1000) {

	//const uint8_t lvl_off = DIGIPOT_MAX_AMOUNT;
	//const uint8_t lvl_on = 10;
	const int8_t lvl_diff = lvl_off-lvl_on;

	// VARIABLES PARA MEDIR EL TIEMPO DE INTEGRACIÓN (DESCOMENTAR EN NECESIDAD)
	// MEDICIÓN DE TIEMPO DE INTEGRACIÓN O w (OPCIONAL)
	int i = 0;
	double* ret_dt = new double[n_meds];
	double * ret_w = new double[n_meds];
	double * ret_v = new double[n_meds];

	const double v_off = 2.505; // Offset de voltaje
	//const double v_att = 0.6734; // Atenuación de voltaje
	const double v_att = 1;
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;

	uint8_t r_level = lvl_off - (uint8_t)rint(w*((float)lvl_diff));

	struct timespec gettime_now;
	double dt, t_prev, t_cur;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->increase(DIGIPOT_MAX_AMOUNT);
	emu01->set(r_level);

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;

	double v = mcp3008_read(1)*v_slope + v_intercept;
	//double lambda = SIGMOID_P(v, a, d);
	double lambda = w; // Para que no se mueva al principio (cond inicial).

	double constante = 1.0e-9/t0;

	while(1)
	{
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		t_cur = gettime_now.tv_nsec;
		dt = t_cur - t_prev;
		

		if (dt<0.0) dt += 1.0e+9;
		//v = mcp3008_read(0)*v_slope + v_intercept;
		//lambda = LAMBDA(v,lambda,a,d);
		//w += (float)dt*1.0e-9*(lambda - w) / (t0*exp(-abs(v) / v0));

		v = mcp3008_read(1)*v_slope + v_intercept;
		lambda = LAMBDA(v,lambda,a_minus, a_plus, d_minus, d_plus);
		//w +=  (dt*constante*(lambda - w)*exp(abs(v)/((double)v0)));
		w = (dt * 1.0e-9 * lambda + w*t0/exp(abs(v)/((double)v0)))/(dt*1.0e-9 + t0/exp(abs(v)/((double)v0)));
		if(w<0) w = 0;
		else if(w>1) w = 1;

		r_level = lvl_off - (uint8_t)rint(((float)w)*((float)lvl_diff));
		emu01->set(r_level);
		//R = RES_MIN+r_level*QUANT_RES;
		
		// MEDICIÓN DE w, tiempo de integración, etc. (DESCOMENTAR EN NECESIDAD)
		//ret_dt[i] = dt;
		//ret_w[i] = w;
		//ret_v[i] = v;
		//if(++i>n_meds) break;
		
		//R = r_diff * w + RES_MAX;
		//emu01->set(uint8_t(rint(((float)(R - RES_MIN)) / ((float)QUANT_RES))));
	}
	
	// IMPRESIÓN DE TIEMPOS DE INTEGRACIÓN o w
	//for(int i=0; i<n_meds;i++) std::cout << ret_dt[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_w[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_v[i] << "\t";
}

//////////////////////////////////////////////////

double sgn(double x){return (x>=0)-(x<0);}
//double Lambert(double x){return log(1+x)*(1-log(1+log(1+x))/(2+log(1+x)));}
double Lambert(double x){return utl::LambertW<0>(x);}
double I_nonlinear(double V, double I0, double a, double Rs){double phi = a*Rs*I0; return sgn(V)*I0*(Lambert(phi*exp(a*abs(V)+phi))/phi-1);}

void modelo_hdpn(double w = 0.5, double eta_m = 1.0, double eta_p = 1.0, double delta_m = 1.0, double delta_p = 1.0, double t0 = 1.0, double v0 = 1.0, double alpha = 1.0, double Rs = 100.0, double I0min = 1.0, double I0max = 1.0, uint8_t lvl_on = 0, uint8_t lvl_off = 99, int n_meds = 100)
{
	//const uint8_t lvl_off	= 80; //20;
	//const uint8_t lvl_on	= 2; //10;
	const uint8_t lvl_diff	= lvl_off-lvl_on;

	const double v_off = 2.505; // Offset de voltaje
	//const double v_att = 0.6734; // Atenuación de voltaje
	const double v_att = 1;
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;
		
	uint8_t r_level = lvl_off - (uint8_t)rint(w*((double)lvl_diff));

	struct timespec gettime_now;
	double dt, t_prev, t_cur;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu_01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu_01->increase(lvl_off);
	emu_01->set(r_level);

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;

	// MEDICIÓN DE TIEMPO DE INTEGRACIÓN O w (OPCIONAL)
	int i = 0;
	double* ret_dt = new double[n_meds];
	//double * ret_w = new double[n_meds];
	//double * ret_v = new double[n_meds];
	//double * ret_I = new double[n_meds];

	double v = mcp3008_read(0)*v_slope + v_intercept;
	double lambda = w; // Para que no se mueva al principio (condición inicial).
	double constante = 1.0e-9/t0;
	double R;

	while(1)
	{
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		t_cur = gettime_now.tv_nsec;
		dt = t_cur - t_prev;
		if (dt<0.0) dt += 1.0e+9;

		v = mcp3008_read(0)*v_slope + v_intercept;
		lambda = LAMBDA(v,lambda,eta_m, eta_p, delta_m, delta_p);
		w +=  (dt*constante*(lambda - w)*exp(abs(v)/((double)v0)));

		if(w<0.0) w = 0.0;
		else if(w>1.0) w = 1.0;

		R = v / I_nonlinear(v,I0min+ w*(I0max-I0min),alpha,Rs);

		r_level = (uint8_t)rint((R-RES_MIN)/QUANT_RES);

		if (r_level < lvl_on) r_level = lvl_on;
		if (r_level > lvl_off) r_level = lvl_off;

		emu_01->set(r_level);
		
		//OPCIONAL: DESCOMENTAR PARA CALCULAR TIEMPO DE INTEGRACIÓN
		//time_dt[time_i++] = dt;
		//if(time_total<time_max)
		//{for(int i=0; i<time_i;i++) std::cout << time_dt[i] << "\t"; break;}

		// MEDICIÓN DE w, tiempo de integración, etc. (DESCOMENTAR EN NECESIDAD)
		//ret_dt[i] = dt;
		//ret_w[i] = w;
		//ret_v[i] = v;
		//ret_I[i] = I_nonlinear(v,I0min+ w*(I0max-I0min),alpha,Rs);
		//if(++i>n_meds) break;
	}
	// IMPRESIÓN DE TIEMPOS DE INTEGRACIÓN o w
	//for(int i=0; i<n_meds;i++) std::cout << ret_dt[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_w[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_v[i] << "\t";
	//for(int i=0; i<n_meds;i++) std::cout << ret_I[i] << "\t";
}

/*
double get_dt(time)
{
	t_prev = t_cur;
	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;
	dt = t_cur - t_prev;
	if (dt<0.0) dt += 1.0e+9;
	return time, dt;
}
*/

//////////////////////////////////////////////////

int reset(void)
{
	wiringPiSetup();

	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	//emu01->reset();
	emu01->increase(DIGIPOT_MAX_AMOUNT);
	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int inc(uint8_t lvls)
{

	wiringPiSetup();

	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->increase(lvls);

	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int dec(uint8_t lvls)
{

	wiringPiSetup();

	std::cout << (float)lvls << "\n";

	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->decrease(lvls);

	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int set_resistance(float res)
{
	uint8_t resvalue;

	wiringPiSetup();

	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	//emu01->reset();
	emu01->increase(DIGIPOT_MAX_AMOUNT);

	std::cout << "Resistencia pedida = " << res << "\n";

	res = (res < RES_MIN) ? RES_MIN : res;
	res = (res > RES_MAX) ? RES_MAX : res;

	resvalue = rintf((res - RES_MIN) / QUANT_RES);
	res = RES_MIN + resvalue * QUANT_RES;

	std::cout << (res - RES_MIN) << std::endl << QUANT_RES << std::endl;

	std::cout << "Resistencia seteada = " << res << "\n";
	std::cout << "Nivel seteado = " << (int)resvalue << "\n";


	emu01->set(resvalue);

	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int mcp3008_read(uint8_t chan)
{
	char cmd[3];
	cmd[0] = starti;
	cmd[1] = (0x08 | chan) << 4;
	cmd[2] = endi;

	char readBuf[3];
	bcm2835_spi_transfernb(cmd, readBuf, 3);
	return ((int)readBuf[1] & 0x03) << 8 | (int)readBuf[2];
}

//////////////////////////////////////////////////

int spi_setup(void)
{
	if (!bcm2835_init())
	{
		std::cout << "bcm2835_init failed. Are you running as root??\n";
		return 1;
	}

	if (!bcm2835_spi_begin())
	{
		std::cout << "bcm2835_spi_begin failed. Are you running as root??\n";
		return 1;
	}
	bcm2835_spi_setBitOrder(BCM2835_SPI_BIT_ORDER_MSBFIRST);      // The default
	bcm2835_spi_setDataMode(BCM2835_SPI_MODE0);                   // The default
	//bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_256);   // ~1 MHz
	bcm2835_spi_setClockDivider(BCM2835_SPI_CLOCK_DIVIDER_64);   								// ~2 MHz
	bcm2835_spi_chipSelect(BCM2835_SPI_CS0);                      // The default
	bcm2835_spi_setChipSelectPolarity(BCM2835_SPI_CS0, LOW);      // the default

	return 0;
}

//////////////////////////////////////////////////

int mcp3008_data(int frequency, int interval, uint8_t channel = 0)
{
	if (spi_setup() != 0)
		return 1;

	struct timespec gettime_now;
	int dt = rintf(1000.0 / ((double)frequency));
	long cant = interval * frequency * 1000;
	long* timesnsecs = new long[cant];
	int* values = new int[cant];

	if (dt < 40)
		dt = 0;

	for (long i = 0; i<cant; i++)
	{
		values[i] = mcp3008_read(channel);
		clock_gettime(CLOCK_REALTIME, &gettime_now);
		timesnsecs[i] = gettime_now.tv_nsec;
		delayMicroseconds(dt);
	}

	//spi.close();
	for (long i = 0; i<cant; i++)
	{
		std::cout << timesnsecs[i] << "\t" << values[i] << std::endl;
	}

	//std::cout << dt;

	delete timesnsecs;
	delete values;
	return 0;
}

//////////////////////////////////////////////////
