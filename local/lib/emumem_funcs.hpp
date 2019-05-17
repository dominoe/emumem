#pragma once

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
		cout << k << "\n";
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

void modelo_hp(double w = 0.5, double mu = 1) {

	const double r_on = 1035.0;
	const double r_diff = r_on - RES_MAX;

	const double v_off = 2.35; // Offset de voltaje
	const double v_att = 0.68; // Atenuación de voltaje
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;

	double I, V, R = RES_MIN;

	uint8_t r_level = 0;

	struct timespec gettime_now;
	float dt, t_prev, t_cur;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	//emu01->reset();
	emu01->increase(DIGIPOT_MAX_AMOUNT);

	emu01->set(50);

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;

	while (1) {
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);

		t_cur = gettime_now.tv_nsec;
		dt = t_cur - t_prev;
		if (dt<0.0) dt += 1.0e+9;
		w += (float)dt*mu*1.0e-9*RES_MAX*(mcp3008_read(0)*v_slope + v_intercept) / R;
		if (w<0) w = 0;
		else if (w>1) w = 1;
		R = r_diff * w + RES_MAX;
		emu01->set(uint8_t(rint(((float)(R - RES_MIN)) / ((float)QUANT_RES))));
	}
}

//////////////////////////////////////////////////

void modelo_hist(double w = 0.5, double mu = 1, float a, float d) {

	const uint8_t lvl_off = DIGIPOT_MAX_AMOUNT;
	const uint8_t lvl_on = 10;
	const uint8_t lvl_diff = lvl_on - lvl_off;

	const double r_off = RES_MIN + QUANT_RES * lvl_off;
	const double r_on = RES_MIN + QUANT_RES * lvl_on;
	const double r_diff = QUANT_RES * lvl_diff;

	const double v_off = 2.35; // Offset de voltaje
	const double v_att = 0.68; // Atenuación de voltaje
	const double v_slope = 5.0 / 1023.0 / v_att;
	const double v_intercept = -v_off / v_att;

	double I, V = VOLT_READ(), R = r_diff * w + RES_MAX;
	double lambda = SIGMOID_M(V, a, d)

		uint8_t r_level = 0;

	struct timespec gettime_now;
	float dt, t_prev, t_cur;

	if (spi_setup() != 0) return;

	wiringPiSetup();
	DigiPot* emu01 = new DigiPot(INCPIN, UDPIN, CSPIN);
	//emu01->reset();
	emu01->increase(DIGIPOT_MAX_AMOUNT);

	emu01->set(round(lvl_diff*w + lvl_off));

	clock_gettime(CLOCK_REALTIME, &gettime_now);
	t_cur = gettime_now.tv_nsec;

	while (1) {
		t_prev = t_cur;
		clock_gettime(CLOCK_REALTIME, &gettime_now);

		t_cur = gettime_now.tv_nsec;
		dt = t_cur - t_prev;
		if (dt<0.0) dt += 1.0e+9;

		V = VOLT_READ();

		lambda = LAMBDA(V, lambda, a, d);
		w += (float)dt*1.0e-9*(lambda - w) / (t0*exp(-abs(V) / v0));

		if (w<0) w = 0;
		else if (w>1) w = 1;
		R = r_diff * w + RES_MAX;
		emu01->set(uint8_t(rint(((float)(R - RES_MIN)) / ((float)QUANT_RES))));
	}
}

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

	cout << (float)lvls << "\n";

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

	cout << "Resistencia pedida = " << res << "\n";

	res = (res < RES_MIN) ? RES_MIN : res;
	res = (res > RES_MAX) ? RES_MAX : res;

	resvalue = rintf((res - RES_MIN) / QUANT_RES);
	res = RES_MIN + resvalue * QUANT_RES;

	cout << (res - RES_MIN) << endl << QUANT_RES << endl;

	cout << "Resistencia seteada = " << res << "\n";
	cout << "Nivel seteado = " << (int)resvalue << "\n";


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
		cout << timesnsecs[i] << "\t" << values[i] << endl;
	}

	//cout << dt;

	delete timesnsecs;
	delete values;
	return 0;
}

//////////////////////////////////////////////////
