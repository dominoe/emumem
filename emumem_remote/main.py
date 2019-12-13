#%%############################################
# CONSTANTES Y PARÁMETROS GLOBALES

CON_GEN_ADDRESS = 'USB0::0x1AB1::0x0641::DG4C150400092::INSTR'
CON_OSC_ADDRESS = 'USB0::0x1AB1::0x0488::DS1BA113200430::INSTR'
CON_PI2_IP = '10.2.40.31'
CON_PI2_PORT = 22
CON_PI2_USER = 'pi'
CON_PI2_PASS = 'memristorpi'

REMOTE_INSTANCE_NAME = 'emumem'

MODELO_NAME = "hdpn_dual" # hp, hdp, hdpn

save_med = True
save_simu = True

RES_MIN = 37.661
RES_MAX = 9402.4
RES_DIF = RES_MAX - RES_MIN
DIGIPOT_MAX_AMOUNT = 99
QUANT_RES = RES_DIF/99

r = [37.661,134.58,231.51,327.72,423.34,518.2,615.65,715.88,810.37,908.23,1004.28,1101.41,1195.08,1290,1384.2,1478.6,1577,1675.7,1772,1858.3,1963.9,2060,2154.9,2249.5,2344.4,2439.6,2536.2,2630.2,2725.7,2818.8,2914.5,3009.7,3102.9,3198.2,3295.8,3387.9,3484.3,3583.1,3681.3,3779.8,3876.3,3971.4,4066.8,4163.1,4257.8,4351.3,4446.8,4543,4637.6,4733.2,4829.7,4923.4,5019.2,5114.3,5209.9,5306.8,5401,5496.7,5593,5686.7,5783.7,5880.1,5973.8,6068,6160.6,6252.9,6344.7,6439,6534.5,6629.3,6724,6819,6911,7007.4,7102.5,7195.3,7289.4,7383.7,7476.8,7570.8,7663.6,7758.1,7852.9,7949,8044.5,8137.7,8233,8325.1,8418.8,8511.4,8602,8695.6,8788.8,8880.9,8975.7,9067.9,9160.5,9251,9338.6,9402.4]

##############################
# MODELO HD ##################

MODELO_HP_W = 0.5
MODELO_HP_MU = 9000

##############################

##############################
# MODELO HDP #################

MODELO_HDP_W = 1
MODELO_HDP_ALPHA = 30
MODELO_HDP_DELTA = 0.75
MODELO_HDP_TAU0 = 20
MODELO_HDP_V0 = 0.2

## HDP labo 6
#MODELO_HDP_W = 0.5 
#MODELO_HDP_ALPHA = 45
#MODELO_HDP_DELTA = 0.2
#MODELO_HDP_TAU0 = 5
#MODELO_HDP_V0 = 0.3

##############################

##############################
# MODELO HDPN ################

#MODELO_HDPN_W = 0.5
#MODELO_HDPN_ETA = 45
#MODELO_HDPN_DELTA = 0.2
#MODELO_HDPN_TAU0 = 0.01
#MODELO_HDPN_ALPHA = 0
#MODELO_HDPN_RS = 1e2
#MODELO_HDPN_V0 = 0.3
#MODELO_HDPN_IOMIN = 3.5e-5
##MODELO_HDPN_IOMAX = 1.9e-4
#MODELO_HDPN_IOMAX = 1e-2
##MODELO_HDPN_IOMIN = 1e-6
##MODELO_HDPN_IOMAX = 2e-4

#MODELO_HDPN_W = 0.5
#MODELO_HDPN_ETA = 30
#MODELO_HDPN_DELTA = 0.45
#MODELO_HDPN_TAU0 = 1e-2
#MODELO_HDPN_ALPHA = 3
#MODELO_HDPN_RS = 1e2
#MODELO_HDPN_V0 = 0.3
#MODELO_HDPN_IOMIN = 3.5e-5
##MODELO_HDPN_IOMAX = 1.9e-4
#MODELO_HDPN_IOMAX = 1e-2
##MODELO_HDPN_IOMIN = 1e-6
##MODELO_HDPN_IOMAX = 2e-4
#
# MAS ABIERTO
MODELO_HDPN_W = 0
MODELO_HDPN_ETA = 30
MODELO_HDPN_DELTA = 0.475
MODELO_HDPN_TAU0 = 20 #20 #0.1
MODELO_HDPN_ALPHA = 1
MODELO_HDPN_RS = 1e2
MODELO_HDPN_V0 = 0.2
#
#MODELO_HDPN_W = 0.5
#MODELO_HDPN_ETA = 30
#MODELO_HDPN_DELTA = 0.75
#MODELO_HDPN_TAU0 = 1400
#MODELO_HDPN_ALPHA = 2
#MODELO_HDPN_RS = 1e2
#MODELO_HDPN_V0 = 0.09

#MODELO_HDPN_I0MIN = 6e-5 # 1k - 5k ? ?
#MODELO_HDPN_I0MAX = 2e-4 # 1k - 5k ? ?

#MODELO_HDPN_IOMIN = 3.5e-5 # 100 - 10k
##MODELO_HDPN_IOMAX = 1.9e-4
#MODELO_HDPN_IOMAX = 1e-2 # 100 - 10k
##MODELO_HDPN_IOMIN = 1e-6
#MODELO_HDPN_IOMAX = 2e-4

MODELO_HDPN_IOMIN = 1.1e-4
MODELO_HDPN_IOMAX = 5.1e-4

##############################

##############################
# MODELO HDPN DUAL ###########

MODELO_HDPN_DUAL_W_1 = 0
MODELO_HDPN_DUAL_ETA_M_1 = 30
MODELO_HDPN_DUAL_ETA_P_1 = 30
MODELO_HDPN_DUAL_DELTA_M_1 = 0.475
MODELO_HDPN_DUAL_DELTA_P_1 = 0.475
MODELO_HDPN_DUAL_TAU0_1 = 500
MODELO_HDPN_DUAL_ALPHA_1 = 1
MODELO_HDPN_DUAL_RS_1 = 1e2
MODELO_HDPN_DUAL_V0_1 = 0.2
MODELO_HDPN_DUAL_IOMIN_1 = 1.1e-4
MODELO_HDPN_DUAL_IOMAX_1 = 5.1e-4

MODELO_HDPN_DUAL_LVL_ON_1 = 10
MODELO_HDPN_DUAL_LVL_OFF_1 = 99

MODELO_HDPN_DUAL_W_2 = 0
MODELO_HDPN_DUAL_ETA_M_2 = 45
MODELO_HDPN_DUAL_ETA_P_2 = 30
MODELO_HDPN_DUAL_DELTA_M_2 = 0.05
MODELO_HDPN_DUAL_DELTA_P_2 = 0.475
MODELO_HDPN_DUAL_TAU0_2 = 3
MODELO_HDPN_DUAL_ALPHA_2 = 1
MODELO_HDPN_DUAL_RS_2 = 1e2
MODELO_HDPN_DUAL_V0_2 = 0.2
MODELO_HDPN_DUAL_IOMIN_2 = 1.1e-4
MODELO_HDPN_DUAL_IOMAX_2 = 5.1e-4

MODELO_HDPN_DUAL_LVL_ON_2 = 10
MODELO_HDPN_DUAL_LVL_OFF_2 = 99

MODELO_HDPN_DUAL_N_MEDS = 500000

##############################

gen_frequency = 0.4 # 1 para hdpn, 2 para STDP
gen_voltage = 2 # 4.5 para hdpn, 3 para STDP
gen_waveform = 'CUST' # CUST, SIN, ...

N_MEDS = 500000

LVL_ON = 10
LVL_OFF = 99 # 99 para hdpn, 52 para STDP
Rc = 1000

# IF CUSTOM WAVEFORM
gen_signal_points = 10000
gen_signal_amp_spike = 1 # 1.0
gen_signal_amp_probe = 0.2 #0.133 , 0.2
gen_signal_width_spike = 10
gen_signal_width_probe = 88 #5 , 80
gen_signal_wait_spike = 1
gen_signal_wait_probe = 50 - (gen_signal_width_probe + gen_signal_width_spike + gen_signal_wait_spike)/2 #35.5 #5.5

# BURST CYCLES
burst_ncycles = 20

#%%############################################
# LIBRERIAS

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import scipy.signal as sig
from scipy.integrate import odeint
from scipy.special import lambertw

import numpy as np
from numpy import pi

from lib.instruments import *
from lib.emu_mod import *
from lib.emu_fun import *

import csv
import time
import re
import os

#%%############################################
# DEFINICIÓN DE CLASES

gen = RIGOL_DG4162()
osc = RIGOL_DS1204B()
raspi_ssh = RASPBERRY_PI2_SSH()
emu_mod = EMU_MOD()
emu_fun = EMU_FUN()

#%%############################################
# CONEXIÓN CON LOS DISTINTOS INSTRUMENTOS

gen.open_instrument(CON_GEN_ADDRESS)
osc.open_instrument(CON_OSC_ADDRESS)
raspi_ssh.connect(CON_PI2_IP, CON_PI2_PORT, CON_PI2_USER, CON_PI2_PASS)

#%%############################################
# CONFIGURACIÓN DEL GENERADOR DE FUNCIONES

#gen_signal = emu_fun.custom_burst_signal(gen_signal_points,gen_signal_wait_probe,gen_signal_wait_spike,gen_signal_width_probe,gen_signal_width_spike,gen_signal_amp_probe,gen_signal_amp_spike)

gen_signal = np.array([list(emu_fun.gen_pavlov_food(10000, 0.3, 1, 20, 2.5, 5))])
#
gen.set_instrument(gen_waveform,gen_frequency,gen_voltage,0.0,0.0,2)

if (gen_waveform == 'CUST'):
    gen.set_signal(gen_signal,2)

gen.set_output(1)

#%%############################################
# PAVLOV

# MODELO HDPN DUAL ###########

MODELO_HDPN_DUAL_W_1 = 0
MODELO_HDPN_DUAL_ETA_M_1 = 30
MODELO_HDPN_DUAL_ETA_P_1 = 30
MODELO_HDPN_DUAL_DELTA_M_1 = 0.475
MODELO_HDPN_DUAL_DELTA_P_1 = 0.475
MODELO_HDPN_DUAL_TAU0_1 = 3
MODELO_HDPN_DUAL_ALPHA_1 = 1
MODELO_HDPN_DUAL_RS_1 = 1e2
MODELO_HDPN_DUAL_V0_1 = 0.2
MODELO_HDPN_DUAL_IOMIN_1 = 1.1e-4
MODELO_HDPN_DUAL_IOMAX_1 = 5.1e-4

MODELO_HDPN_DUAL_LVL_ON_1 = 10
MODELO_HDPN_DUAL_LVL_OFF_1 = 99

MODELO_HDPN_DUAL_W_2 = 0
MODELO_HDPN_DUAL_ETA_M_2 = 15
MODELO_HDPN_DUAL_ETA_P_2 = 30
MODELO_HDPN_DUAL_DELTA_M_2 = 0.01
MODELO_HDPN_DUAL_DELTA_P_2 = 1.3
MODELO_HDPN_DUAL_TAU0_2 = 7
MODELO_HDPN_DUAL_ALPHA_2 = 1
MODELO_HDPN_DUAL_RS_2 = 1e2
MODELO_HDPN_DUAL_V0_2 = 0.2
MODELO_HDPN_DUAL_IOMIN_2 = 1.1e-4
MODELO_HDPN_DUAL_IOMAX_2 = 5.1e-4

MODELO_HDPN_DUAL_LVL_ON_2 = 10
MODELO_HDPN_DUAL_LVL_OFF_2 = 99

MODELO_HDPN_DUAL_N_MEDS = 500000

###

first = 0 # Si es la primera medición, poner 1

pavlov_total_time = 2.5
pavlov_duty_cycle = 0.3
pavlov_amp = 1
pavlov_pulse_freq = 20
pavlov_pulse_train_size = 5

gen_signal_food = np.array([list(emu_fun.gen_pavlov_food(gen_signal_points, pavlov_duty_cycle, pavlov_amp, pavlov_pulse_freq, pavlov_total_time, pavlov_pulse_train_size))])
gen_signal_bell = np.array([list(emu_fun.gen_pavlov_bell(gen_signal_points, pavlov_duty_cycle, pavlov_amp, pavlov_pulse_freq, pavlov_total_time, pavlov_pulse_train_size))])

gen.set_instrument('CUST',1/pavlov_total_time,gen_voltage,0.0,0.0,1)
gen.set_signal(gen_signal_bell,1)
gen.set_instrument('CUST',1/pavlov_total_time,gen_voltage,0.0,0.0,2)
gen.set_signal(gen_signal_food,2)


if (first):
    scale = gen_voltage/2*pavlov_amp/4
    
    try:
        osc.set_v_scale(1,scale) # 0.05
    except:
        print("")
    
    try:
        osc.set_v_scale(2,scale)
    except:
        print("")
        
    try:
        osc.set_v_scale(3,scale)
    except:
        print("")
        
    try:
        osc.set_v_scale(4,2)
    except:
        print("")
    
    try:
#        osc.set_t_scale(0.5/gen_frequency)
        osc.set_t_scale(pavlov_total_time/12)
    except:
        print("")
        
    t_scale = osc.get_t_scale()
    
    try:
        osc.set_t_offset(5*t_scale)
    except:
        print("")
        
    try:
        osc.set_v_offset(1,-3.4*scale)
    except:
        print("")
    try:
        osc.set_v_offset(2,-3.4*scale)
    except:
        print("")
    try:
        osc.set_v_offset(3,-3*scale)
    except:
        print("")
    try:
        osc.set_v_offset(4,0)
    except:
        print("")

    try:
        osc.set_trig_lvl(gen_voltage/2*pavlov_amp*0.95)
    except:
        print("")

# Se hace antes.
gen.burst_signal(1,cycles=1)
gen.burst_signal(2,cycles=1)
gen.trig_source(2,"EXT")
gen.trig_source(1,"MANUAL")

file_str = "data/PAVLOV_fr_" + str(pavlov_pulse_freq) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")

if (MODELO_NAME == "hp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hp {0} {1} {2} {3} {4} &'.format(MODELO_HP_W, MODELO_HP_MU, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} &'.format(MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn_dual"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn_dual {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26}&'.format(MODELO_HDPN_DUAL_W_1, MODELO_HDPN_DUAL_ETA_M_1, MODELO_HDPN_DUAL_ETA_P_1, MODELO_HDPN_DUAL_DELTA_M_1, MODELO_HDPN_DUAL_DELTA_P_1, MODELO_HDPN_DUAL_TAU0_1, MODELO_HDPN_DUAL_V0_1, MODELO_HDPN_DUAL_ALPHA_1, MODELO_HDPN_DUAL_RS_1, MODELO_HDPN_DUAL_IOMIN_1, MODELO_HDPN_DUAL_IOMAX_1, MODELO_HDPN_DUAL_LVL_ON_1, MODELO_HDPN_DUAL_LVL_OFF_1, MODELO_HDPN_DUAL_W_2, MODELO_HDPN_DUAL_ETA_M_2, MODELO_HDPN_DUAL_ETA_P_2, MODELO_HDPN_DUAL_DELTA_M_2, MODELO_HDPN_DUAL_DELTA_P_2, MODELO_HDPN_DUAL_TAU0_2, MODELO_HDPN_DUAL_V0_2, MODELO_HDPN_DUAL_ALPHA_2, MODELO_HDPN_DUAL_RS_2, MODELO_HDPN_DUAL_IOMIN_2, MODELO_HDPN_DUAL_IOMAX_2, MODELO_HDPN_DUAL_LVL_ON_2, MODELO_HDPN_DUAL_LVL_OFF_2, MODELO_HDPN_DUAL_N_MEDS))

raspi_ssh.wait(5) # Cambié de 10 a 5.

try:
    osc.single()
except:
    print("")

sleep(5)
gen.trigger()

sleep(t_scale*15) #8

osc_time_1, osc_data_1 = osc.get_channel(1)
osc_time_2, osc_data_2 = osc.get_channel(2)
osc_time_3, osc_data_3 = osc.get_channel(3)
osc_time_4, osc_data_4 = osc.get_channel(4)

raspi_ssh.kill_instances(REMOTE_INSTANCE_NAME)
gen.burst_off(1)

plt.figure(1)
plt.clf()
plt.plot(osc_time_1, osc_data_1)
plt.plot(osc_time_2, osc_data_2)
plt.plot(osc_time_3, osc_data_3)
plt.plot(osc_time_4, osc_data_4)

fig, axs = plt.subplots(4, 1)
axs[0].plot(osc_time_1, osc_data_1)
axs[1].plot(osc_time_2, osc_data_2)
axs[2].plot(osc_time_3, osc_data_3)
axs[3].plot(osc_time_4, osc_data_4)

axs[0].set_title('Comida')
axs[0].set_xlabel('Tiempo (s)')
axs[0].set_ylabel('Tensión (V)')
axs[1].set_title('Campana')
axs[1].set_xlabel('Tiempo (s)')
axs[1].set_ylabel('Tensión (V)')
axs[2].set_title('Neurona')
axs[2].set_xlabel('Tiempo (s)')
axs[2].set_ylabel('Tensión (V)')
axs[3].set_title('Saliva')
axs[3].set_xlabel('Tiempo (s)')
axs[3].set_ylabel('Tensión (V)')

axs[0].grid(True)
axs[1].grid(True)
axs[2].grid(True)
axs[3].grid(True)

axs[0].set_xlim(-2.5, 0.5)
axs[1].set_xlim(-2.5, 0.5)
axs[2].set_xlim(-2.5, 0.5)
axs[3].set_xlim(-2.5, 0.5)

fig.tight_layout()
plt.show()

plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')

#%%############################################
# ADQUISICIÓN DE PULSOS (REQUIERE PANTALLA EN STOP)

first = 1 # Si es la primera medición, poner 1

if (first):
    scale = gen_voltage/2*gen_signal_amp_probe/4
    
    try:
        osc.set_v_scale(1,scale) # 0.05
    except:
        print("")
    
    try:
        osc.set_v_scale(2,scale)
    except:
        print("")
    
    try:
#        osc.set_t_scale(0.5/gen_frequency)
        osc.set_t_scale(burst_ncycles/10/gen_frequency)
    except:
        print("")
        
    t_scale = osc.get_t_scale()
    
    try:
        osc.set_t_offset(5*t_scale)
    except:
        print("")
        
    try:
        osc.set_v_offset(1,-3.4*scale)
    except:
        print("")
    try:
        osc.set_v_offset(2,-3.4*scale)
    except:
        print("")

    try:
        osc.set_trig_lvl(gen_voltage/2*gen_signal_amp_probe*0.95)
#        print(osc.get_trig_lvl())
    except:
        print("")

# Se hace antes.
gen.burst_signal(1,burst_ncycles)
gen.trig_source(1,"MANUAL")

file_str = "data/STDP_modelo_" + MODELO_NAME + "_fr_" + str(gen_frequency) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")

if (MODELO_NAME == "hp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hp {0} {1} {2} {3} {4} &'.format(MODELO_HP_W, MODELO_HP_MU, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} &'.format(MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn_dual"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn_dual {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26}&'.format(MODELO_HDPN_DUAL_W_1, MODELO_HDPN_DUAL_ETA_M_1, MODELO_HDPN_DUAL_ETA_P_1, MODELO_HDPN_DUAL_DELTA_M_1, MODELO_HDPN_DUAL_DELTA_P_1, MODELO_HDPN_DUAL_TAU0_1, MODELO_HDPN_DUAL_V0_1, MODELO_HDPN_DUAL_ALPHA_1, MODELO_HDPN_DUAL_RS_1, MODELO_HDPN_DUAL_IOMIN_1, MODELO_HDPN_DUAL_IOMAX_1, MODELO_HDPN_DUAL_LVL_ON_1, MODELO_HDPN_DUAL_LVL_OFF_1, MODELO_HDPN_DUAL_W_2, MODELO_HDPN_DUAL_ETA_M_2, MODELO_HDPN_DUAL_ETA_P_2, MODELO_HDPN_DUAL_DELTA_M_2, MODELO_HDPN_DUAL_DELTA_P_2, MODELO_HDPN_DUAL_TAU0_2, MODELO_HDPN_DUAL_V0_2, MODELO_HDPN_DUAL_ALPHA_2, MODELO_HDPN_DUAL_RS_2, MODELO_HDPN_DUAL_IOMIN_2, MODELO_HDPN_DUAL_IOMAX_2, MODELO_HDPN_DUAL_LVL_ON_2, MODELO_HDPN_DUAL_LVL_OFF_2, MODELO_HDPN_DUAL_N_MEDS))

raspi_ssh.wait(5) # Cambié de 10 a 5.

try:
    osc.single()
except:
    print("")

sleep(5)
gen.trigger()

sleep(t_scale*15) #8

osc_time_1, osc_data_1 = osc.get_channel(1)
osc_time_2, osc_data_2 = osc.get_channel(2)

raspi_ssh.kill_instances(REMOTE_INSTANCE_NAME)
gen.burst_off(1)

plt.figure(1)
plt.clf()
plt.plot(osc_time_1, osc_data_1)
plt.plot(osc_time_2, osc_data_2)

plt.xlabel('Tiempo (s)')
plt.ylabel('Tensión (V)')

#%%############################################
# ADQUISICIÓN DE PARÁMETROS DE TEST DEL MODELO

TIME_ONLY = False

from scipy.optimize import curve_fit

def seno(x, a, f, p, o):
     return a*np.sin(2*pi*f*x-p) + o

if (MODELO_NAME == "hp"):
    output = raspi_ssh.execute('sudo nice -n-20 ./emumem/emumem modelo_hp {0} {1} {2} {3} {4} &'.format(MODELO_HP_W, MODELO_HP_MU, LVL_ON, LVL_OFF, N_MEDS))
elif (MODELO_NAME == "hdp"):
    output = raspi_ssh.execute('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, LVL_ON, LVL_OFF, N_MEDS))
elif (MODELO_NAME == "hdpn"):
    output = raspi_ssh.execute('sudo nice -n-20 ./emumem/emumem modelo_hdpn {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} &'.format(MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, LVL_ON, LVL_OFF, N_MEDS))
elif (MODELO_NAME == "hdpn_dual"):
    output = raspi_ssh.execute('sudo nice -n-20 ./emumem/emumem modelo_hdpn_dual {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26}&'.format(MODELO_HDPN_DUAL_W_1, MODELO_HDPN_DUAL_ETA_M_1, MODELO_HDPN_DUAL_ETA_P_1, MODELO_HDPN_DUAL_DELTA_M_1, MODELO_HDPN_DUAL_DELTA_P_1, MODELO_HDPN_DUAL_TAU0_1, MODELO_HDPN_DUAL_V0_1, MODELO_HDPN_DUAL_ALPHA_1, MODELO_HDPN_DUAL_RS_1, MODELO_HDPN_DUAL_IOMIN_1, MODELO_HDPN_DUAL_IOMAX_1, MODELO_HDPN_DUAL_LVL_ON_1, MODELO_HDPN_DUAL_LVL_OFF_1, MODELO_HDPN_DUAL_W_2, MODELO_HDPN_DUAL_ETA_M_2, MODELO_HDPN_DUAL_ETA_P_2, MODELO_HDPN_DUAL_DELTA_M_2, MODELO_HDPN_DUAL_DELTA_P_2, MODELO_HDPN_DUAL_TAU0_2, MODELO_HDPN_DUAL_V0_2, MODELO_HDPN_DUAL_ALPHA_2, MODELO_HDPN_DUAL_RS_2, MODELO_HDPN_DUAL_IOMIN_2, MODELO_HDPN_DUAL_IOMAX_2, MODELO_HDPN_DUAL_LVL_ON_2, MODELO_HDPN_DUAL_LVL_OFF_2, MODELO_HDPN_DUAL_N_MEDS))


arr_out = re.split('\t', output)

arr_t = np.array([float(s) for s in arr_out[:N_MEDS]])
arr_t2 = [0]
for i,t in enumerate(arr_t):
    arr_t2.append(arr_t2[i]+t*1e-9)
arr_t2 = np.array(arr_t2)[1:]
if (not TIME_ONLY):
    if (MODELO_NAME == "hp"):
        arr_w = np.array([float(s) for s in arr_out[N_MEDS:2*N_MEDS]])
    elif (MODELO_NAME == "hdpn" or MODELO_NAME == "hdp"):
        arr_w = np.array([float(s) for s in arr_out[N_MEDS:2*N_MEDS]])
        arr_v = np.array([float(s) for s in arr_out[2*N_MEDS:3*N_MEDS]])
        
        arr_bits = np.round((arr_v+2.505/0.6734)/(5/1023/0.6734))
        #cociente = arr_bits/volt_mem
    
        plt.figure(1)
        plt.clf()
        plt.plot(arr_v,arr_w)
        plt.xlabel ('V en memristor')
        plt.ylabel ('Lambda')
        
        if (MODELO_NAME == "hdpn"):
            arr_i = np.array([float(s) for s in arr_out[3*N_MEDS:-1]])
            plt.figure(2)
            plt.clf()
            plt.plot(arr_t2,arr_v,'.-', label="Voltaje")
            plt.plot(arr_t2,arr_i*1000,'.-', label="Corriente")
            plt.plot(arr_t2,arr_v/arr_i,'.-', label="Resistencia")
            plt.legend()
            plt.xlabel ('Tiempo (s)')
            plt.ylabel ('Corriente')
            
        popt, pcov = curve_fit(seno, arr_t2, arr_v, p0=(3.5,gen_frequency,1.5,0))
        popt2, pcov2 = curve_fit(seno, arr_t2, arr_bits, p0=(200,gen_frequency,1.5,500))
        popt3, pcov3 = curve_fit(seno, osc_time_1, volt_mem, p0=(3.5,gen_frequency,1.5,0))
        popt4, pcov4 = curve_fit(seno, osc_time_1, volt_mem2, p0=(1,gen_frequency,1.5,0))
        
        plt.figure(3)
        plt.clf()
        plt.plot(arr_t2,arr_v)
        plt.plot(arr_t2,seno(arr_t2, *popt))
        plt.xlabel ('Tiempo (s)')
        plt.ylabel ('V en memristor')
        
        plt.figure(4)
        plt.clf()
        plt.plot(arr_t2,arr_bits)
        plt.plot(arr_t2,seno(arr_t2, *popt2))
        plt.xlabel ('Tiempo (s)')
        plt.ylabel ('V en ADC')
        
        plt.figure(5)
        plt.clf()
        plt.plot(osc_time_1,volt_mem)
        plt.plot(osc_time_1,seno(osc_time_1, *popt3))
        plt.xlabel ('Tiempo (s)')
        plt.ylabel ('V en OSC')
        
        plt.figure(6)
        plt.clf()
        plt.plot(osc_time_1,volt_mem2)
        plt.plot(osc_time_1,seno(osc_time_1, *popt4))
        plt.xlabel ('Tiempo (s)')
        plt.ylabel ('V en OSC (MCP)')
        
        print (popt)
    
    
    plt.figure(7)
    plt.clf()
    plt.plot(arr_t2,arr_w,'.-')
    plt.xlabel ('Tiempo (s)')
    plt.ylabel ('Lambda')
    
    alfa = popt3[0]/popt2[0]
    alfa2 = popt4[0]/popt2[0]
    beta = -popt3[0]*popt2[3]/popt2[0]
    beta2 = -popt4[0]*popt2[3]/popt2[0]

raspi_ssh.wait(2)

raspi_ssh.kill_instances('emumem')

#%%############################################

try:
    osc.run()
except:
    print("")

if (MODELO_NAME == "hp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hp {0} {1} {2} {3} {4} &'.format(MODELO_HP_W, MODELO_HP_MU, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdp"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} &'.format(MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, LVL_ON, LVL_OFF, 999999))
elif (MODELO_NAME == "hdpn_dual"):
    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn_dual {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} {12} {13} {14} {15} {16} {17} {18} {19} {20} {21} {22} {23} {24} {25} {26}&'.format(MODELO_HDPN_DUAL_W_1, MODELO_HDPN_DUAL_ETA_M_1, MODELO_HDPN_DUAL_ETA_P_1, MODELO_HDPN_DUAL_DELTA_M_1, MODELO_HDPN_DUAL_DELTA_P_1, MODELO_HDPN_DUAL_TAU0_1, MODELO_HDPN_DUAL_V0_1, MODELO_HDPN_DUAL_ALPHA_1, MODELO_HDPN_DUAL_RS_1, MODELO_HDPN_DUAL_IOMIN_1, MODELO_HDPN_DUAL_IOMAX_1, MODELO_HDPN_DUAL_LVL_ON_1, MODELO_HDPN_DUAL_LVL_OFF_1, MODELO_HDPN_DUAL_W_2, MODELO_HDPN_DUAL_ETA_M_2, MODELO_HDPN_DUAL_ETA_P_2, MODELO_HDPN_DUAL_DELTA_M_2, MODELO_HDPN_DUAL_DELTA_P_2, MODELO_HDPN_DUAL_TAU0_2, MODELO_HDPN_DUAL_V0_2, MODELO_HDPN_DUAL_ALPHA_2, MODELO_HDPN_DUAL_RS_2, MODELO_HDPN_DUAL_IOMIN_2, MODELO_HDPN_DUAL_IOMAX_2, MODELO_HDPN_DUAL_LVL_ON_2, MODELO_HDPN_DUAL_LVL_OFF_2, MODELO_HDPN_DUAL_N_MEDS))

try:
    osc.set_t_scale(0.5/gen_frequency)
except:
    print("")

try:
    osc.set_t_offset(0)
except:
    print("")

try:
    osc.set_v_offset(1,0)
except:
    print("")
    
try:
    osc.set_v_offset(2,0)
except:
    print("")

try:
    osc.set_v_scale(1,gen_voltage/8)
except:
    print("")

try:
    osc.set_v_scale(2,gen_voltage/8)
except:
    print("")

raspi_ssh.wait(5)

try:
    osc.stop()
except:
    print("")
osc_time_1, osc_data_1 = osc.get_channel(1)
osc_time_2, osc_data_2 = osc.get_channel(2)
#osc_time_3, osc_data_3 = osc.get_channel(3)
try:
    osc.run()
except:
    print("")

raspi_ssh.kill_instances(REMOTE_INSTANCE_NAME)
    
volt_mem = osc_data_2 # MIDIENDO EN MEMRISTOR
#volt_mem = osc_data_1 - osc_data_2 # MIDIENDO EN R DE CARGA
#volt_mem2 = (osc_data_3)

#%% GUARDAR MEDICIONES

if not os.path.isdir('data/20191205'):
    os.mkdir('data/' + time.strftime("%Y%m%d"))

file_str = "data/"+time.strftime("%Y%m%d")+"/modelo_" + MODELO_NAME + "_fr_" + str(gen_frequency) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")

with open(file_str+".txt", 'w') as txtFile:
    if (MODELO_NAME == "hdpn_dual"):
        txtFile.write("Eta_m_1: " + str(MODELO_HDPN_DUAL_ETA_M_1) + "Eta_p_1: " + str(MODELO_HDPN_DUAL_ETA_P_1) + "\nDelta_m_1: " + str(MODELO_HDPN_DUAL_DELTA_M_1) + "\nDelta_p_1: " + str(MODELO_HDPN_DUAL_DELTA_P_1) + "\n" + 
                      "Tau0_1: " + str(MODELO_HDPN_DUAL_TAU0_1) + "\nv0_1: " + str(MODELO_HDPN_DUAL_V0_1) + "\n" + 
                      "Alpha_1: " + str(MODELO_HDPN_DUAL_ALPHA_1) + "\nI0min_1: " + str(MODELO_HDPN_DUAL_IOMIN_1) + "\nI0max_1: " + 
                      str(MODELO_HDPN_DUAL_IOMAX_1)  + "\nRs_1: " + str(MODELO_HDPN_DUAL_RS_1) + 
                      "\n\nEta_m_2: " + str(MODELO_HDPN_DUAL_ETA_M_2) + "Eta_p_2: " + str(MODELO_HDPN_DUAL_ETA_P_2) + "\nDelta_m_2: " + str(MODELO_HDPN_DUAL_DELTA_M_2) + "\nDelta_p_1: " + str(MODELO_HDPN_DUAL_DELTA_P_1) + "\n" + 
                      "Tau0_2: " + str(MODELO_HDPN_DUAL_TAU0_2) + "\nv0_2: " + str(MODELO_HDPN_DUAL_V0_2) + "\n" + 
                      "Alpha_2: " + str(MODELO_HDPN_DUAL_ALPHA_2) + "\nI0min_2: " + str(MODELO_HDPN_DUAL_IOMIN_2) + "\nI0max_2: " + 
                      str(MODELO_HDPN_DUAL_IOMAX_2)  + "\nRs_2: " + str(MODELO_HDPN_DUAL_RS_2) +
                      "\n\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\n\nLVL_ON_1: " + str(MODELO_HDPN_DUAL_LVL_ON_1) + "\nLVL_OFF_1: " + str(MODELO_HDPN_DUAL_LVL_OFF_1) + 
                      "\n\nLVL_ON_2: " + str(MODELO_HDPN_DUAL_LVL_ON_2) + "\nLVL_OFF_2: " + str(MODELO_HDPN_DUAL_LVL_OFF_2))
    if (MODELO_NAME == "hdpn"):
        txtFile.write("Eta: " + str(MODELO_HDPN_ETA) + "\nDelta: " + str(MODELO_HDPN_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + "\n" + 
                      "Alpha: " + str(MODELO_HDPN_ALPHA) + "\nI0min: " + str(MODELO_HDPN_IOMIN) + "\nI0max: " + 
                      str(MODELO_HDPN_IOMAX)  + "\nRs: " + str(MODELO_HDPN_RS) + "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    if (MODELO_NAME == "hdp"):
        txtFile.write("Cond inicial (w0): " + str(MODELO_HDP_W) + "\nAlpha: " + str(MODELO_HDP_ALPHA) + "\nDelta: " + str(MODELO_HDP_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + 
                      "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    if (MODELO_NAME == "hp"):
        txtFile.write("Cond inicial (w0): " + str(MODELO_HP_W) + "\nMu: " + str(MODELO_HP_MU) +
                      "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
txtFile.close()
if (osc_data_3.any() and osc_data_4.any()):
    np.save(file_str,np.array([osc_time_1,osc_data_1,osc_data_2,osc_data_3,osc_data_4]))
else:
    np.save(file_str,np.array([osc_time_1,osc_data_1,osc_data_2]))

#%%
# CÓDIGO PARA EVALUAR CAÍDA DE TENSIÓN SEGÚN: MCP, OSC EN CARGA Y OSC EN MCP
#
#from scipy.optimize import curve_fit
#
#import datetime
#date_today = str(datetime.date.today())
#
#def seno(x, a, f, p, o):
#     return a*np.sin(2*pi*f*x-p) + o
# 
#def fit_alfa_doble(V, a1, a2):
#    v1,v2 = V
#    return a1*v1 - a2*v2
#
#v_adc = []
#v_carga_osc = []
#v_gen_osc = []
#v_mcp_osc = []
#
#offs_adc = []
#
#for res in range(100):
#    raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, res, res, N_MEDS))
#    
#    try:
#        osc.set_t_scale(0.5/gen_frequency)
#    except:
#        print("")
#    
#    raspi_ssh.wait(2)
#    
#    try:
#        osc.stop()
#    except:
#        print("")
#    osc_time_1, osc_data_1 = osc.get_channel(1)
#    osc_time_2, osc_data_2 = osc.get_channel(2)
#    osc_time_3, osc_data_3 = osc.get_channel(3)
#    try:
#        osc.run()
#        print("")
#    except:
#    
#    raspi_ssh.kill_instances(REMOTE_INSTANCE_NAME)
#    
#    raspi_ssh.wait(1)
#    
#    output = raspi_ssh.execute('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, res, res, N_MEDS))
#    
#    arr_out = re.split('\t', output)
#    
#    arr_t = np.array([float(s) for s in arr_out[:N_MEDS]])
#    arr_t2 = [0]
#    for i,t in enumerate(arr_t):
#        arr_t2.append(arr_t2[i]+t*1e-9)
#    arr_t2 = np.array(arr_t2)[1:]
#    arr_v = np.array([float(s) for s in arr_out[2*N_MEDS:3*N_MEDS]])
#        
#    arr_bits = np.round((arr_v+2.505)/(5/1023))
#        
#    popt_adc, pcov_adc = curve_fit(seno, arr_t2, arr_bits, p0=(200,gen_frequency,1.5,500))
#    popt_carga_osc, pcov_carga_osc = curve_fit(seno, osc_time_1, osc_data_2, p0=(2,gen_frequency,1.5,0))
#    popt_gen_osc, pcov_gen_osc = curve_fit(seno, osc_time_1, osc_data_1, p0=(2,gen_frequency,1.5,0))
#    popt_mcp_osc, pcov_mcp_osc = curve_fit(seno, osc_time_1, osc_data_3, p0=(2,gen_frequency,1.5,0))
#    
#    v_adc.append(np.abs(popt_adc[0]))
#    v_carga_osc.append(np.abs(popt_carga_osc[0]))
#    v_gen_osc.append(np.abs(popt_gen_osc[0]))
#    v_mcp_osc.append(np.abs(popt_mcp_osc[0]))
#    
#    offs_adc.append(popt_adc[3])
#
#v_adc = np.array(v_adc)
#v_carga_osc = np.array(v_carga_osc)
#v_gen_osc = np.array(v_gen_osc)
#v_mcp_osc = np.array(v_mcp_osc)
#offs_adc = np.array(offs_adc)
#
#alfa_p0 = np.abs((v_gen_osc - v_carga_osc)/v_adc)
#popt_alfas_carga, pcov_alfas_carga = curve_fit(fit_alfa_doble, (v_gen_osc,v_carga_osc), v_adc, p0=(alfa_p0[50],alfa_p0[50]))
#    
#perr_alfas_carga = np.sqrt(np.diag(pcov_alfas_carga))
#perr_alfa_gen = perr_alfas_carga[0]
#perr_alfa_carga = perr_alfas_carga[1]
#
#alfa_gen = popt_alfas_carga[0]
#alfa_carga = popt_alfas_carga[1]
#
#alfa_mcp = v_mcp_osc/v_adc
#beta_mcp = v_mcp_osc*offs_adc/v_adc
#
#np.save("./data/conversion_adc_vs_res/" + date_today + "/beta_mcp", beta_mcp)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/alfa_mcp", alfa_mcp)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/alfa_carga", alfa_carga)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/alfa_gen", alfa_gen)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/perr_alfa_gen", perr_alfa_gen)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/perr_alfa_carga", perr_alfa_carga)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/offs_adc", offs_adc)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/v_mcp_osc", v_mcp_osc)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/v_carga_osc", v_carga_osc)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/v_gen_osc", v_gen_osc)
#np.save("./data/conversion_adc_vs_res/" + date_today + "/v_adc", v_adc)
#%%############################################
# DETECCIÓN Y MEDICIÓN DE PROBES DEL GENERADOR

from scipy.signal import find_peaks
from scipy.signal import peak_widths

t = osc_time_1
v = osc_data_1
vmem = osc_data_2
i = (v - vmem) / Rc

num_meds = len(t)
gen_period = 1/gen_frequency
acq_time = max(t)-min(t)
points_in_period = int(round(num_meds*(gen_period/acq_time))) # Se usa para mejorar la búsqueda de probes, así busca uno solo por periodo.


est_voltage_spike = gen_voltage*gen_signal_amp_spike/2
est_voltage_probe  = (gen_voltage/2)*gen_signal_amp_probe

#tolerance_spike = 0.1
tolerance_probe_min = 0.5
tolerance_probe_max = 0.3

#tolerance_probe_min_up = 0.5
#tolerance_probe_max_up = 0.3

est_width_probe = points_in_period*gen_signal_width_probe/100

tolerance_width = 0.1

max_width_probe = est_width_probe*(1.0+tolerance_width)
min_width_probe = est_width_probe*(1.0-tolerance_width)

#max_voltage_spike = est_voltage_spike*(1.0+tolerance_spike)
#min_voltage_spike = est_voltage_spike*(1.0-tolerance_spike)

max_voltage_probe = est_voltage_probe*(1.0+tolerance_probe_max)
min_voltage_probe = est_voltage_probe*(1.0-tolerance_probe_min)

#maxs_spike,_ = find_peaks(np.diff(v),height=(min_voltage_spike,max_voltage_spike))
#mins_spike,_ = find_peaks(-np.diff(v),height=(min_voltage_spike,max_voltage_spike))

#begin_probes,_ = find_peaks(np.diff(v),height=(min_voltage_probe,max_voltage_probe),distance=(points_in_period*0.95,points_in_period*1.05))
#end_probes,_ = find_peaks(-np.diff(v),height=(min_voltage_probe,max_voltage_probe),distance=(points_in_period*0.95,points_in_period*1.05))

#v = v[707+338:]
#t = t[707+338:]
#vmem = vmem[707+338:]

peak_probes,_ = find_peaks(v,height=(min_voltage_probe,max_voltage_probe),distance=points_in_period*0.95,width=(min_width_probe,max_width_probe))
#end_probes,_ = find_peaks(-np.diff(v),height=(min_voltage_probe,max_voltage_probe),distance=points_in_period*0.95,width=(min_width_probe,max_width_probe))

width_probes = peak_widths(v, peak_probes, rel_height=0.2)

#begin_spikes_pre = maxs_spike[::2]
#end_spikes_pre = mins_spike[::2]
#end_spikes_post = maxs_spike[1::2]
#begin_spikes_post = mins_spike[1::2]

#plt.plot(v)
#plt.plot(peak_probes, v[peak_probes], "x")
#plt.hlines(*width_probes[1:], color="C2")
#plt.show()

if not (len(peak_probes) == burst_ncycles):
    print("Hubo un problema en la búsqueda de picos, intentar de nuevo.")

plt.figure("pulsos")
plt.clf()
plt.xlabel("Tiempo (s)")
plt.ylabel("Tensión (V)")
#plt.plot(t,v,t,vmem)
plt.plot(v)
plt.plot(vmem)

v_mean = []
v_se = []
vmem_mean = []
vmem_se = []
i_mean = []
i_se = []

t = np.linspace(0,len(t),len(t))
plt.plot(t[peak_probes],vmem[peak_probes],markersize=12,marker='o')

for c in range(burst_ncycles):
    plt.plot(t,vmem)
    plt.plot(t[int(width_probes[2][c])+1:int(width_probes[3][c])],vmem[int(width_probes[2][c])+1:int(width_probes[3][c])],'.')
    v_mean.append(np.mean(v[int(width_probes[2][c])+1:int(width_probes[3][c])]))
    v_se.append(np.std(v[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))
    vmem_mean.append(np.mean(vmem[int(width_probes[2][c])+1:int(width_probes[3][c])]))
    vmem_se.append(np.std(vmem[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))
    i_mean.append(np.mean(i[int(width_probes[2][c])+1:int(width_probes[3][c])]))
    i_se.append(np.std(i[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))


v_mean = np.array(v_mean)
vmem_mean = np.array(vmem_mean)
i_mean = np.array(i_mean)
v_se = np.array(v_se)
vmem_se = np.array(vmem_se)
i_se = np.array(i_se)

r_mean = vmem_mean/i_mean
r_se = r_mean * np.sqrt((vmem_se/vmem_mean)**2+(i_se/i_mean)**2)

if (MODELO_NAME == "hdp"):
    tau0_str = str(MODELO_HDP_TAU0)
    mod_str = "lineal"
elif (MODELO_NAME == "hdpn"):
    tau0_str = str(MODELO_HDPN_TAU0)
    mod_str = "no lineal"

plt.figure("Resistencias")
plt.clf()
plt.errorbar (np.linspace(0,(burst_ncycles-1)*gen_period,burst_ncycles), r_mean, r_se, fmt='o')
plt.grid()
plt.xlabel("Tiempo (s)")
plt.ylabel("Resistencia ($\Omega$)")
plt.title("Modelo " + mod_str + " $\Delta$t = " + str(gen_signal_wait_spike/100*gen_period*1000) + "ms, $\\tau _0$ = " + tau0_str + "s")

#%% GUARDAR PROBES

file_str = "data/STDP/r_vs_pulse/STDP_" + MODELO_NAME + "_fr_" + str(gen_frequency) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")

with open(file_str+".txt", 'w') as txtFile:
    if (MODELO_NAME == "hdpn"):
        txtFile.write("Eta: " + str(MODELO_HDPN_ETA) + "\nDelta: " + str(MODELO_HDPN_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + "\n" + 
                      "Alpha: " + str(MODELO_HDPN_ALPHA) + "\nI0min: " + str(MODELO_HDPN_IOMIN) + "\nI0max: " + 
                      str(MODELO_HDPN_IOMAX)  + "\nRs: " + str(MODELO_HDPN_RS) + "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    if (MODELO_NAME == "hdp"):
        txtFile.write("Cond inicial (w0): " + str(MODELO_HDP_W) + "\nAlpha: " + str(MODELO_HDP_ALPHA) + "\nDelta: " + str(MODELO_HDP_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + 
                      "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    if (MODELO_NAME == "hp"):
        txtFile.write("Cond inicial (w0): " + str(MODELO_HP_W) + "\nMu: " + str(MODELO_HP_MU) +
                      "\nFrecuencia: " + str(gen_frequency) + "\n" + 
                      "Amplitud (VPP): " + str(gen_voltage) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    txtFile.write("\nAmplitud relativa spike: " + str(gen_signal_amp_spike) + "\nAmplitud relativa probe: " + str(gen_signal_amp_probe) + 
                  "\nAncho spike: " + str(gen_signal_width_spike/gen_frequency*10) + "ms\nAncho probe: " + 
                  str(gen_signal_width_probe/gen_frequency*10) + "ms\nDelta t (invertido): " + str(gen_signal_wait_spike/gen_frequency*10) + "ms")

txtFile.close()

np.save(file_str,np.array([np.linspace(0,(burst_ncycles-1)*gen_period,burst_ncycles),r_mean,r_se]))

#%%############################################
###### MEDICIÓN DE CURVAS CONVERGENCIA R VS DELTA T Y TAU 0 ######

from lib.lib_stdp import acq_pulses
from lib.lib_stdp import process_pulses

gen.set_instrument('CUST',gen_frequency,gen_voltage,0.0,0.0)

stdp_num_reps = 5

gen_signal_wait_spike = 20
gen_signal_wait_probe = 50 - (gen_signal_width_probe + gen_signal_width_spike + gen_signal_wait_spike)/2 #35.5 #5.5

r_vals = []
err_vals = []

#i_t0 = 0 ## IMPORTANTE!! CAMBIAR MANUALMENTE
#tau_0 = 20 # 20, 10, 5

cycles_tau = [np.repeat(6,28),np.repeat(6,28),np.repeat(6,28)]

#cycles_tau = [np.array([7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]),
#              np.array([12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 14, 14, 15, 16, 16, 15, 14, 14, 13, 13, 13, 12, 12, 12, 12, 12, 12, 12]),
#              np.array([22, 22, 22, 22, 22, 23, 26, 27, 29, 31, 33, 36, 40, 43, 43, 40, 36, 33, 31, 29, 27, 26, 23, 22, 22, 22, 22, 22])
#              ]

#for i_dt, delta_t in enumerate(np.concatenate(([-40, -30, -20,-15],np.linspace(-10,-1,10),np.linspace(1,10,10),[15,20,30,40]))):

for i_t0, tau_0 in enumerate([20,50,200]):
    r_vals.append([])
    err_vals.append([])
    hdp_params = [MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, tau_0, MODELO_HDP_V0, LVL_ON, LVL_OFF, N_MEDS]
    hdpn_params = [MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, tau_0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, LVL_ON, LVL_OFF, N_MEDS]
    for i_dt, delta_t in enumerate(np.concatenate(([-40,-30,-20,-15],np.linspace(-10,-1,10),np.linspace(1,10,10),[15,20,30,40]))):
        gs_wait_probe = 50 - (gen_signal_width_probe + gen_signal_width_spike + delta_t)/2 #35.5 #5.5
        
        gen_signal = emu_fun.custom_burst_signal(gen_signal_points,gs_wait_probe,delta_t,gen_signal_width_probe,gen_signal_width_spike,gen_signal_amp_probe,gen_signal_amp_spike)
        
        gen.set_signal(gen_signal)
        gen.set_output(1)
        
        med = 0
        r_vals[i_t0].append([])
        err_vals[i_t0].append([])
        while med < stdp_num_reps:
            print("Comenzando nueva medición. tau0 =", tau_0, "delta t =", delta_t, "(índice", i_dt, "), medición", med)
            t, v, _, v_mem = acq_pulses(osc, gen, raspi_ssh, gen_frequency, gen_voltage, MODELO_NAME, hdpn_params, med==0, cycles_tau[i_t0][i_dt], gen_signal_amp_probe)
            proc = process_pulses(t,v,v_mem, Rc, est_voltage=(gen_voltage/2)*gen_signal_amp_probe, est_width=gen_signal_width_probe, freq=gen_frequency, n_cycles=cycles_tau[i_t0][i_dt], tolerance_min=0.5, tolerance_max=0.2, tolerance_width=0.1)
            if proc:
                r_mean, r_se = proc
#                r_vals[i_t0][i_dt].append(r_mean[-5:]) # TOMAR LOS ULTIMOS 5 PUNTOS
#                err_vals[i_t0][i_dt].append(np.sqrt(np.var(r_mean[-5:])+np.mean(np.square(r_se[-5:])))) # TOMAR LOS ULTIMOS 5 PUNTOS
                r_vals[i_t0][i_dt].append(r_mean[-1:])
                err_vals[i_t0][i_dt].append(r_se[-1:])
                np.save("data/STDP/ventana_aprendizaje/HDPN/tau" + str(tau_0) + "/dt_" + str(delta_t) + "_r_mean_med_" + str(med) + ".npy", r_vals)
                np.save("data/STDP/ventana_aprendizaje/HDPN/tau" + str(tau_0) + "/dt_" + str(delta_t) + "_r_se_med_" + str(med) + ".npy", err_vals)
                med += 1
        
#    r_vals_mean = np.empty(0)
#    r_vals_std = np.empty(0)
#    se_vals_mean = np.empty(0)
#            
#    for r_val in r_vals[2]:
#        r_vals_mean = np.append(r_vals_mean, np.mean(r_val))
#        r_vals_std = np.append(r_vals_std, np.std(r_val))
#    
#    for se_val in se_vals[2]:
#        se_vals_mean = np.append(se_vals_mean, np.sqrt(np.mean(np.array(se_val)**2)))
#    
#    r_error = np.sqrt(r_vals_std**2+se_vals_mean**2)
#
#plt.figure("Conv. R vs Delta t")
##plt.clf()
#plt.errorbar(5*np.concatenate(([-40, -30, -20,-15],np.linspace(-10,-1,10),np.linspace(1,10,10),[15,20,30,40])),list(reversed(r_vals_mean)),list(reversed(r_error)), fmt='o')
#plt.xlabel("$\Delta$t")
#plt.ylabel("Resistencia")
#%%############################################

MODELO_HDPN_DUAL_W_2 = 0
MODELO_HDPN_DUAL_ETA_M_2 = 15
MODELO_HDPN_DUAL_ETA_P_2 = 30
MODELO_HDPN_DUAL_DELTA_M_2 = 0.01
MODELO_HDPN_DUAL_DELTA_P_2 = 1
MODELO_HDPN_DUAL_TAU0_2 = 10
MODELO_HDPN_DUAL_ALPHA_2 = 1
MODELO_HDPN_DUAL_RS_2 = 1e2
MODELO_HDPN_DUAL_V0_2 = 0.2
MODELO_HDPN_DUAL_IOMIN_2 = 1.1e-4
MODELO_HDPN_DUAL_IOMAX_2 = 5.1e-4

Ron = r[LVL_ON]
Roff = r[LVL_OFF]
#Roff = 9486.0

w0 = MODELO_HP_W

f = 20
v0 = 2.5/2

s = max(osc_time_1)
dt = 20e-6
t = np.linspace(0, s, s/dt)
v = v0*np.cos(2*pi*f*t)+0.75

if (MODELO_NAME == "hp"):
    m,w_debug = emu_mod.hp(t, v, w0, MODELO_HP_MU, Rc, LVL_ON, LVL_OFF)
if (MODELO_NAME == "hdp"):
    m,w_debug = emu_mod.histeron(t, v, w0, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, Rc, LVL_ON, LVL_OFF)
if (MODELO_NAME == "hdpn"):
    m,w_debug,lamb_debug = emu_mod.histeron_nonlinear(t, v, w0, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, Rc, Ron, Roff)
if (MODELO_NAME == "hdpn_dual"):
    m,w_debug,lamb_debug = emu_mod.histeron_nonlinear(t, v, w0, MODELO_HDPN_DUAL_ETA_M_2, MODELO_HDPN_DUAL_ETA_P_2, MODELO_HDPN_DUAL_DELTA_M_2, MODELO_HDPN_DUAL_DELTA_P_2, MODELO_HDPN_DUAL_TAU0_2, MODELO_HDPN_DUAL_V0_2, MODELO_HDPN_DUAL_ALPHA_2, MODELO_HDPN_DUAL_RS_2, MODELO_HDPN_DUAL_IOMIN_2, MODELO_HDPN_DUAL_IOMAX_2, Rc, Ron, Roff)

#m_hdpn,_,_ = emu_mod.histeron_nonlinear(t, v, w0, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, Rc, Ron, Roff)
#i_hdpn = v / (Rc + m_hdpn)

i = v / (Rc + m)

#%% GUARDAR DATOS
if (save_simu):
    if not os.path.isdir('data/20191018'):
        os.mkdir('data/' + time.strftime("%Y%m%d"))

    file_str = "data/"+time.strftime("%Y%m%d")+"/modelo_" + MODELO_NAME + "_fr_" + str(gen_frequency) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")
    np.save(file_str,np.array([t,v,m]))

#%% PLOTS

import scipy.signal as signal

# First, design the Buterworth filter

#N  = 1    # Filter order
#Wn = .5 # Cutoff frequency
#B, A = signal.butter(N, Wn, output='ba')
#volt_mem_smooth = signal.filtfilt(B,A, volt_mem)
#gen_smooth = signal.filtfilt(B,A, osc_data_1)
#
#current_smooth = (gen_smooth-volt_mem_smooth)/Rc*1000

#plt.plot(volt_mem,'r-')
#plt.plot(volt_mem_smooth,current_smooth,'b.')
#plt.show()

from scipy import stats

plt.figure(7)
plt.clf()

# EXP
#slope_exp, intercept_exp, r_value_exp, p_value_exp, std_err_exp = stats.linregress(volt_mem,osc_data_2/1000)
#plt.plot(volt_mem_smooth,current_smooth, '.', color=(0,0,1,0.3), label = "Experimental")

#plt.plot(volt_mem, ((osc_data_1-osc_data_2)/Rc*1000), '.', color=(0,0,1,0.3), label = "Experimental")

# SIM
#slope_sim, intercept_sim, r_value_sim, p_value_sim, std_err_sim = stats.linregress(i[t>s/2]*m[t>s/2],i[t>s/2])
plt.plot(i[t>s/8]*m[t>s/8],(i[t>s/8]*1000), color=(1,0.3,0.2,1), label = "Simulación")
#plt.plot(i_hdpn[t>s/2]*m_hdpn[t>s/2],i_hdpn[t>s/2])
#plt.semilogy(osc_data_1 - osc_data_2, np.abs(osc_data_2/1000),'.')
#plt.semilogy(i[t>s/2]*m[t>s/2],np.abs(i[t>s/2]))
plt.legend()
plt.xlabel('Tensión (V)', fontsize = 15)
plt.ylabel('Corriente (mA)', fontsize = 15)
plt.grid()

#plt.plot(t[t>s/2],w[t>s/2])
#plt.plot(t[t>s/2],m[t>s/2])
#plt.plot(t[t>s/2],Iev[t>s/2],t[t>s/2],v[t>s/2]/1000)

#%% TODO ESTO LO AGREGUÉ PARA MIRAR ALGUNAS COSAS. SE PUEDE COMENTAR TODO, SE PUEDE BORRAR; QUÉ SÉ YO.

DELAY = 0.0232

plt.figure(8)
plt.clf()
#plt.plot(osc_time_1, (osc_data_1 - osc_data_2)/osc_data_2*1000, osc_time_1,osc_data_2*2000,osc_time_1,osc_data_1*2000)
plt.plot(osc_time_1,osc_data_1*2000,'--', label='Referencia')
plt.plot(osc_time_1,osc_data_2*2000,'--')
plt.plot(osc_time_1, (osc_data_1 - osc_data_2)/osc_data_2*1000, label='Experimental')
plt.plot(t[t>s/2]-DELAY, m[t>s/2], label='Simulación')
plt.plot(t[t>s/2]-DELAY, v[t>s/2]*2000, label='REF Simulación')
plt.xlabel("Tiempo (s)")
plt.ylabel("Resistencia ($\Omega$)")
plt.legend()

plt.figure(9)
plt.clf()
plt.plot(osc_time_1,osc_data_2, label='Experimental')
plt.plot(t[t>s/2]-DELAY, i[t>s/2]*1000, label='Simulación')
plt.xlabel("Tiempo (s)")
plt.ylabel("Corriente (mA)")
plt.legend()

plt.figure(10)
plt.clf()
smooth_simu = sig.savgol_filter(i[t>s/2]*1000,55,2)
smooth_exp = sig.savgol_filter(osc_data_2,55,2)
plt.plot(t[t>s/2]-DELAY, smooth_simu, label='Simulación')
plt.plot(osc_time_1, smooth_exp, label='Experimental')

d_smooth_simu = sig.savgol_filter(np.gradient(smooth_simu,1),55,2)

dd_smooth_simu = sig.savgol_filter(np.gradient(d_smooth_simu,1),155,2)

plt.plot(t[t>s/2]-DELAY, dd_smooth_simu*10000, label='Simulación (2da der.)')

plt.xlabel("Tiempo (s)")
plt.ylabel("Corriente (mA)")
plt.legend()

plt.figure(11)
plt.clf()
plt.plot(t[t>s/2], w_debug[t[1:]>s/2], label='Simulación')
plt.plot(t[t>s/2], v[t>s/2])
