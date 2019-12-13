import matplotlib.pyplot as plt
import numpy as np

from scipy.special import lambertw

from lib.emu_fun import *

MODELO_NAME = "hdpn"

RES_MIN = 37.661
RES_MAX = 9402.4
RES_DIF = RES_MAX - RES_MIN
DIGIPOT_MAX_AMOUNT = 99
QUANT_RES = RES_DIF/99

MODELO_HDP_W = 0
MODELO_HDP_ALPHA = 30
MODELO_HDP_DELTA = 0.75
MODELO_HDP_TAU0 = 1
MODELO_HDP_V0 = 0.2

MODELO_HDPN_W = 0
MODELO_HDPN_ETA = 30
MODELO_HDPN_DELTA = 0.75
MODELO_HDPN_TAU0 = 200
MODELO_HDPN_ALPHA = 1
MODELO_HDPN_RS = 1e2
MODELO_HDPN_V0 = 0.2

#MODELO_HDPN_IOMIN = 3.5e-5 # 100 - 10k
#MODELO_HDPN_IOMAX = 1e-2 # 100 - 10k

#MODELO_HDPN_IOMIN = 5.4e-5 # 100 - 10k
#MODELO_HDPN_IOMAX = 1e-4 # 100 - 10k

MODELO_HDPN_IOMIN = 1.05e-4
MODELO_HDPN_IOMAX = 2.8e-4

Rc = 1000

LVL_ON = 10
LVL_OFF = 99

f = 2
v0 = 5/2
dt = 20e-5

r = [37.661,134.58,231.51,327.72,423.34,518.2,615.65,715.88,810.37,908.23,1004.28,1101.41,1195.08,1290,1384.2,1478.6,1577,1675.7,1772,1858.3,1963.9,2060,2154.9,2249.5,2344.4,2439.6,2536.2,2630.2,2725.7,2818.8,2914.5,3009.7,3102.9,3198.2,3295.8,3387.9,3484.3,3583.1,3681.3,3779.8,3876.3,3971.4,4066.8,4163.1,4257.8,4351.3,4446.8,4543,4637.6,4733.2,4829.7,4923.4,5019.2,5114.3,5209.9,5306.8,5401,5496.7,5593,5686.7,5783.7,5880.1,5973.8,6068,6160.6,6252.9,6344.7,6439,6534.5,6629.3,6724,6819,6911,7007.4,7102.5,7195.3,7289.4,7383.7,7476.8,7570.8,7663.6,7758.1,7852.9,7949,8044.5,8137.7,8233,8325.1,8418.8,8511.4,8602,8695.6,8788.8,8880.9,8975.7,9067.9,9160.5,9251,9338.6,9402.4]

Ron = r[LVL_ON]
Roff = r[LVL_OFF]

s = 3

t = np.linspace(0, s, s/dt)
v = v0*np.cos(2*np.pi*f*t)

# IF CUSTOM WAVEFORM
gen_signal_points = int(len(t)/(f*s))
gen_signal_amp_spike = 1 # 1.0 #.46 para HDPN
gen_signal_amp_probe = 0.133 #0.33
gen_signal_width_spike = 10
gen_signal_width_probe = 5 #35
gen_signal_wait_spike = -1
gen_signal_wait_probe = 50 - (gen_signal_width_probe + gen_signal_width_spike + gen_signal_wait_spike)/2 #35.5 #5.5

# BURST CYCLES
burst_ncycles = 16

emu_fun = EMU_FUN()

gen_signal = emu_fun.custom_burst_signal(gen_signal_points,gen_signal_wait_probe,gen_signal_wait_spike,gen_signal_width_probe,gen_signal_width_spike,gen_signal_amp_probe,gen_signal_amp_spike)

signal = v0*np.tile(gen_signal[0],f*s)+0.001

def SIGMOID_M(v,a,d):
        return 1.0 / (1.0 + np.exp(-a * (v + d)))
    
def SIGMOID_P(v,a,d):
    return 1.0 / (1.0 + np.exp(-a * (v - d)))

def LAMBDA(v,old,a,d):
    return min(SIGMOID_M(v,a,d), max(old, SIGMOID_P(v,a,d)))

def Lambert(x):
    #return np.log(1+x)*(1-np.log(1+np.log(1+x))/(2+np.log(1+x)))
    return lambertw(x)

def I_nonlinear(V, I0, a, Rs):
    phi = a*Rs*I0
    return np.sign(V)*I0*(Lambert(phi*np.exp(a*np.abs(V)+phi))/phi-1)

def histeron_nonlinear(t, v, w = 0.5, eta = 1, delta = 1, t0 = 1, v0 = 1, alpha = 1, Rs = 100, I0min = 1, I0max = 1, Rc = 1000, Ron=30, Roff=10000):    
        V_debug = []
        w_debug = []
        R_debug = []
        I_debug = []
        lamb_debug = []
        
        R = []
        R.append(Roff - round(w*(Roff-Ron)))
        #        lamb = SIGMOID_P(v[0], eta, delta)
        lamb = w
    
        # You probably won't need this if you're embedding things in a tkinter plot...
        plt.ion()

        fig = plt.figure("Histerón")
        ax = fig.add_subplot(111)
        line1, = ax.plot(v[0]*R[0]/(R[0]+Rc), w, 'ro') # Returns a tuple of line objects, thus the comma
        line2, = ax.plot(v[0]*R[0]/(R[0]+Rc), lamb, 'bo')
        v_tira = np.linspace(-max(v),max(v),200)
        plt.plot(v_tira,SIGMOID_M(v_tira,eta,delta))
        plt.plot(v_tira,SIGMOID_P(v_tira,eta,delta))
#        plt.xlim(-10, 10)
#        plt.ylim(-10, 10)

        
        for i in range(len(t)-1):
            dt = t[i+1]-t[i]
            
#            if (i >= 1 and v[i]-v[i-1] > 1):
#                print("PULSO")
            
            V = v[i]*R[i]/(R[i]+Rc)
#            V_debug.append(V)
            lamb = LAMBDA(V, lamb, eta, delta)
            lamb_debug.append(lamb)
            w += dt*(lamb - w) / (t0/np.exp(abs(V) / v0))
#            w += dt*(lamb - w) / (t0)

            
            if (w<0):
                w = 0
            elif (w>1):
                w = 1
            
            w_debug.append(w)
            
            R_cur = V / I_nonlinear(V, I0min + w * (I0max - I0min), alpha, Rs)
            if R_cur < Ron:
              R_cur   = Ron
            if R_cur > Roff:
                R_cur = Roff
            
            R.append(R_cur)
            R_debug.append(R[i+1])
            I_debug.append(V/R[i+1])
            
#            if (not i%10):
#                line1.set_xdata(V)
#                line1.set_ydata(w)
#                line2.set_xdata(V)
#                line2.set_ydata(lamb)
#                fig.canvas.draw()
#                fig.canvas.flush_events()
#            
        return np.array(R),w_debug,lamb_debug, np.array(I_debug)
    
def histeron(t, v, w = 0.5, a = 1, d = 1, t0 = 1, v0 = 1, Rc = 1000, lvl_on=0, lvl_off=99):
        lvl_diff = lvl_off - lvl_on
    
    #    r_off = RES_MIN + QUANT_RES * lvl_off
    #    r_on = RES_MIN + QUANT_RES * lvl_on
    #    r_diff = QUANT_RES * lvl_diff
    
    #    v_off = 2.5 # Offset de voltaje
    #    v_att = 0.68 # AtenuaciÃ³n de voltaje
    #    v_slope = 5.0 / 1023.0 / v_att
    #    v_intercept = -v_off / v_att
        w_debug = []
        R = []
        lamb_debug = []
        r_level = lvl_off - round(w*lvl_diff)
        R.append(RES_MIN+r_level*QUANT_RES)
        lamb = w
        
        # You probably won't need this if you're embedding things in a tkinter plot...
        plt.ion()

        fig = plt.figure("Histerón")
        ax = fig.add_subplot(111)
        line1, = ax.plot(v[0]*R[0]/(R[0]+Rc), w, 'ro') # Returns a tuple of line objects, thus the comma
        line2, = ax.plot(v[0]*R[0]/(R[0]+Rc), lamb, 'bo')
        v_tira = np.linspace(-max(v),max(v),200)
        plt.plot(v_tira,SIGMOID_M(v_tira,a,d))
        plt.plot(v_tira,SIGMOID_P(v_tira,a,d))
        
        for i in range(len(t)-1):
            dt = t[i+1]-t[i]
            
            V = v[i]*R[i]/(R[i]+Rc)
            
            lamb = LAMBDA(V, lamb, a, d)
            lamb_debug.append(lamb)
#           w += dt*(lamb - w) / (t0/np.exp(abs(V) / v0))
            w = (dt * lamb + (t0/np.exp(abs(V) / v0)) * w)/(dt + (t0/np.exp(abs(V) / v0)))
            
            if (w<0):
                w = 0
            elif (w>1):
                w = 1
            w_debug.append(w)
            r_level = lvl_off - round(w*lvl_diff)
#            r_level = lvl_off - w*lvl_diff
            R.append(RES_MIN+r_level*QUANT_RES)
            
#            if (not i%2):
#                line1.set_xdata(V)
#                line1.set_ydata(w)
#                line2.set_xdata(V)
#                line2.set_ydata(lamb)
#                fig.canvas.draw()
#                fig.canvas.flush_events()
#            
        return np.array(R), np.array(w_debug), np.array(lamb_debug)

def ventana_aprendizaje():
    res_points = np.empty(0)
    dt_array = np.concatenate(([-40,-30,-20,-15],np.linspace(-10,-1,10),np.linspace(1,10,10),[15,20,30,40]))
    for i_dt, delta_t in enumerate(dt_array):
        gen_signal = emu_fun.custom_burst_signal(gen_signal_points,gen_signal_wait_probe,delta_t,gen_signal_width_probe,gen_signal_width_spike,gen_signal_amp_probe,gen_signal_amp_spike)

        signal = v0*np.tile(gen_signal[0],f*s)+0.001
        if (MODELO_NAME == "hdpn"):
            res,w_deb,l_deb, I_deb = histeron_nonlinear(t, signal, MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, Rc, Ron, Roff)
        if (MODELO_NAME == "hdp"):
            res,w_deb,l_deb = histeron(t,signal,MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, Rc, LVL_ON, LVL_OFF)
        res_points = np.append(res_points, np.mean(res[(f*s-1)*gen_signal_points+1:int(gen_signal_points*((f*s-1)+gen_signal_width_probe/100))]))
    plt.figure("Ventana de aprendizaje")
    plt.plot(dt_array*5,res_points,'o')
    plt.xlabel("Tiempo de espera (ms)")
    plt.ylabel("Valor de convergencia de R ($\Omega$)")
    plt.grid()
    return dt_array, res_points

if __name__=="__main__":
    if (MODELO_NAME == "hdpn"):
        res,w_deb,l_deb, I_deb = histeron_nonlinear(t, signal, MODELO_HDPN_W, MODELO_HDPN_ETA, MODELO_HDPN_DELTA, MODELO_HDPN_TAU0, MODELO_HDPN_V0, MODELO_HDPN_ALPHA, MODELO_HDPN_RS, MODELO_HDPN_IOMIN, MODELO_HDPN_IOMAX, Rc, Ron, Roff)
    if (MODELO_NAME == "hdp"):
        res,w_deb,l_deb = histeron(t,signal,MODELO_HDP_W, MODELO_HDP_ALPHA, MODELO_HDP_DELTA, MODELO_HDP_TAU0, MODELO_HDP_V0, Rc, LVL_ON, LVL_OFF)
    plt.figure("Simulaciones")
#    plt.plot(res)
    res_points = np.empty(0)
    for i in range(f*s):
        res_points = np.append(res_points, np.mean(res[i*gen_signal_points+1:int(gen_signal_points*(i+gen_signal_width_probe/100))]))
    plt.plot(np.linspace(0,f*s-1,f*s)/f,res_points,'o--')
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Resistencia ($\Omega$)")
    plt.grid()
    
#%%    FIGURAS PARA MIRAR EVOLUCIÓN DE PARÁMETROS
    
    plt.figure("Resistencia")
    plt.plot(res,'-')
    plt.plot(signal*5000,'.-')
    plt.xlabel("Medición")
    plt.ylabel("Resistencia")
    plt.grid()
    
    plt.figure("Lambda")
    plt.plot(l_deb,'-')
    plt.xlabel("Medición")
    plt.ylabel("$\lambda$")
    plt.grid()
    
    plt.figure("Histerón vs med")
    plt.plot(w_deb,'-')
    plt.xlabel("Medición")
    plt.ylabel("Histerón (w)")
    plt.grid()
    
    plt.figure("Corriente")
    plt.plot(I_deb*1000,'-')
    plt.xlabel("Medición")
    plt.ylabel("Corriente (mA)")
    plt.grid()
    
    
#%% GUARDAR PROBES
    
import time

file_str = "data/STDP/r_vs_pulse/SIM_STDP_" + MODELO_NAME + "_fr_" + str(f) + "_volt_" + str(v0*2) + "_" + time.strftime("%Y%m%d-%H%M%S")

with open(file_str+".txt", 'w') as txtFile:
    if (MODELO_NAME == "hdpn"):
        txtFile.write("Eta: " + str(MODELO_HDPN_ETA) + "\nDelta: " + str(MODELO_HDPN_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + "\n" + 
                      "Alpha: " + str(MODELO_HDPN_ALPHA) + "\nI0min: " + str(MODELO_HDPN_IOMIN) + "\nI0max: " + 
                      str(MODELO_HDPN_IOMAX)  + "\nRs: " + str(MODELO_HDPN_RS) + "\nFrecuencia: " + str(f) + "\n" + 
                      "Amplitud (VPP): " + str(v0*2) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
    if (MODELO_NAME == "hdp"):
        txtFile.write("Cond inicial (w0): " + str(MODELO_HDP_W) + "\nAlpha: " + str(MODELO_HDP_ALPHA) + "\nDelta: " + str(MODELO_HDP_DELTA) + "\n" + 
                      "Tau0: " + str(MODELO_HDPN_TAU0) + "\nv0: " + str(MODELO_HDPN_V0) + 
                      "\nFrecuencia: " + str(f) + "\n" + 
                      "Amplitud (VPP): " + str(v0*2) + "\nLVL_ON: " + str(LVL_ON) + "\nLVL_OFF: " + str(LVL_OFF))
txtFile.close()

np.save(file_str,np.array([np.linspace(0,f*s-1,f*s)/f,res_points]))