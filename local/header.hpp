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
#include "lib/DigiPotX9Cxxx-vRPi.h"

#include "lib/err_hand.hpp"
#include "lib/emumem_funcs.hpp"

using namespace std;

//////////////////////////////////////////////////
// CONSTANTES ////////////////////////////////////
//////////////////////////////////////////////////

const int RES_MIN = 35;
const int RES_MAX = 10035;
const int LEVELS = 100;
const float QUANT_RES = (RES_MAX - RES_MIN) / (LEVELS - 1.0);

const uint8_t starti = 0x01;
const uint8_t endi = 0x00;

//////////////////////////////////////////////////
// MACROS ////////////////////////////////////////
//////////////////////////////////////////////////

#define INCPIN	0
#define UDPIN		1
#define CSPIN		4

#define SIGMOID_M(v,a,d) 1 / (1 + exp(-a * (v - d)))
#define SIGMOID_P(v,a,d) 1 / (1 + exp(-a * (v + d)))
#define LAMBDA(v,old,a,d) fmin(SIGMOID_M(v,a,d), fmax(old, SIGMOID_P(v,a,d)))

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
void modelo_hp(double, double);

//////////////////////////////////////////////////

void exit_success(std::string);
void exit_failure(std::string);
void flush_message(std::string);
bool try_subroutine(std::string, int);
static struct { int argc; std::string name; std::vector<std::string> argv; } Subroutine;