//////////////////////////////////////////////////
// EMUMEM LOCAL (2019-04-27) /////////////////////
//////////////////////////////////////////////////

//////////////////////////////////////////////////
// BIBLIOTECAS ///////////////////////////////////
//////////////////////////////////////////////////

#include <stdint.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <math.h>
#include <wiringPi.h>
#include <bcm2835.h>
#include "DigiPotX9Cxxx-vRPi.h"

using namespace std;

//////////////////////////////////////////////////
// CONSTANTES ////////////////////////////////////
//////////////////////////////////////////////////

#define RES_MIN			35.0
#define RES_MAX			10034.0
#define LEVELS			100
#define QUANT_RES		(RES_MAX-RES_MIN)/(LEVELS-1.0)

#define INCPIN	0
#define UDPIN		1
#define CSPIN		4

const uint8_t starti = 0x01;
const uint8_t endi = 0x00;

//////////////////////////////////////////////////
// PROTOTIPOS ////////////////////////////////////
//////////////////////////////////////////////////

int run_mem(void);
int spi_setup(void);
int reset(void);
int inc(float lvls);
int dec(float lvls);
int set_resistance(float res);
int mcp3008_read(uint8_t chan);
int mcp3008_data(int frequency, int interval, uint8_t channel);
void modelo_hp(double, double);

//////////////////////////////////////////////////

void exit_success(std::string);
void exit_failure(std::string);
void flush_message(std::string);
bool try_subroutine(std::string, int);
static struct {int argc; std::string name; std::vector<std::string> argv;} Subroutine;

//////////////////////////////////////////////////
// MAIN Y SUBRUTINAS /////////////////////////////
//////////////////////////////////////////////////

int main(int argc, char* argv[])
{
	if(argc==1) exit_failure("Error Fatal: El modo de uso es 'main <comando>'");
	
	Subroutine.name = argv[1];
	Subroutine.argc =  argc-2;
	std::copy(argv+2, argv+argc, std::back_inserter(Subroutine.argv));

	if(try_subroutine("reset",0)) reset();
	if(try_subroutine("inc_resistance",1)) inc(std::stof(Subroutine.argv[0]));
	if(try_subroutine("dec_resistance",1)) dec(std::stof(Subroutine.argv[0]));
	if(try_subroutine("set_resistance",1)) set_resistance(std::stof(Subroutine.argv[0]));
	if(try_subroutine("adq_mcp",3)) mcp3008_data(std::stoi(Subroutine.argv[0]), std::stoi(Subroutine.argv[1]), std::stoi(Subroutine.argv[2]));
	if(try_subroutine("modelo_hp",2)) modelo_hp(std::stod(Subroutine.argv[0]), std::stod(Subroutine.argv[1]));

	exit_success("El programa ha finalizado correctamente");
}

//////////////////////////////////////////////////
// CONTROL DE ERRORES ////////////////////////////
//////////////////////////////////////////////////

void flush_message(std::string message){
	std::cout << message << std::endl;}

void exit_failure(std::string message){
	flush_message(message);
	exit(EXIT_FAILURE);}

void exit_success(std::string message){
	flush_message(message);
	exit(EXIT_SUCCESS);}

bool try_subroutine(std::string name, int argc){
	if(name.compare(Subroutine.name) != 0) return false;
	if(argc != Subroutine.argc) exit_success("Error Fatal: La subrutina llamada debe tener " + std::to_string(argc) + " argumentos propios.");
	return true;}

//////////////////////////////////////////////////
// FUNCIONES GENERALES ///////////////////////////
//////////////////////////////////////////////////

int run_mem(void){

	wiringPiSetup();
	
	
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->reset();

	for(int k=0; k<100; k++){
		emu01->increase(1);
		delay(200);
		cout << k << "\n";
	}
	
	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

void modelo_hp(double w = 0.5, double mu = 1){

	// I = V/res = (mcp3008_read(0)*v_slope+v_intercept)/res

	const double r_on = 1035.0;
	const double r_diff = r_on-RES_MAX;

	const double v_off = 2.35;
	const double v_att = 0.68;
	const double v_slope = 5.0/1023.0/v_att;
	const double v_intercept = -v_off/v_att;

	double I, V, R=RES_MIN;
	
	uint8_t r_level = 0;
	
	struct timespec gettime_now;
	float dt, t_prev, t_cur;

	if(spi_setup()!= 0) return;
	
	wiringPiSetup();
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->reset();
	
	emu01->set(50);

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;
	
	while (1) {
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);

		t_cur = gettime_now.tv_nsec;
		dt = t_cur-t_prev;
		if(dt<0.0) dt+=1.0e+9;
		w += (float)dt*mu*1.0e-9*RES_MAX*(mcp3008_read(0)*v_slope+v_intercept)/R;
		if(w<0) w=0;
		else if(w>1) w=1;
		R = r_diff*w+RES_MAX;
		emu01->set(uint8_t(rint(((float)(R-RES_MIN))/((float)QUANT_RES))));
	}
}

//////////////////////////////////////////////////

int reset(void)
{
	wiringPiSetup();
	
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->reset();
	
	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int inc(float lvls)
{

	wiringPiSetup();
	
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	emu01->increase(lvls);
	
	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int dec(float lvls)
{
	
	wiringPiSetup();
	
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
	emu01->reset();

	cout << "Resistencia pedida = " << res << "\n";

	res = (res < RES_MIN)?RES_MIN:res;
	res = (res > RES_MAX)?RES_MAX:res;

	resvalue = rintf((res-RES_MIN)/QUANT_RES);
	res = RES_MIN + resvalue*QUANT_RES;

	cout << "Resistencia seteada = " << res << "\n";
	cout << "Nivel seteado = " << (int) resvalue << "\n";

	
	emu01->set(resvalue);
	
	delete emu01;
	return 0;
}

//////////////////////////////////////////////////

int mcp3008_read(uint8_t chan)
{
	char cmd[3];
	cmd[0] = starti;
	cmd[1] = (0x08|chan)<<4;
	cmd[2] = endi;
		
	char readBuf[3];
	bcm2835_spi_transfernb(cmd,readBuf,3);
	return ((int)readBuf[1] & 0x03) << 8 | (int) readBuf[2];
}

//////////////////////////////////////////////////

int spi_setup(void)
{
	if (!bcm2835_init())
    {
      cout << "bcm2835_init failed. Are you running as root??\n";
      return 1;
    }

    if (!bcm2835_spi_begin())
    {
      cout << "bcm2835_spi_begin failed. Are you running as root??\n";
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
	if( spi_setup() != 0 )
		return 1;
	
	struct timespec gettime_now;
	int dt = rintf(1000.0/((double)frequency));
	long cant = interval*frequency*1000;
	long* timesnsecs = new long[cant];
	int* values  = new int[cant];

	if( dt < 40 )
		dt = 0;
	
    for(long i=0;i<cant;i++)
    {
        values[i] = mcp3008_read(channel);
        clock_gettime(CLOCK_REALTIME, &gettime_now);
		timesnsecs[i] = gettime_now.tv_nsec;
        delayMicroseconds(dt);
    }
    
    //spi.close();
    for(long i=0;i<cant;i++)
    {
		cout << timesnsecs[i] << "\t" << values[i] << endl;
    }

    //cout << dt;
    
    delete timesnsecs;
    delete values;
    return 0;
}

//////////////////////////////////////////////////