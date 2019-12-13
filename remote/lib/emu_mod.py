######################################################
### ULTIMA MODIFICACIÓN: 2019-06-27
######################################################

import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import scipy.signal as sig
from scipy.integrate import odeint
from scipy.special import lambertw

import numpy as np
from numpy import pi

import csv
import time
import re

RES_MIN = 37.661
RES_MAX = 9402.4
RES_DIF = RES_MAX - RES_MIN
DIGIPOT_MAX_AMOUNT = 99
QUANT_RES = RES_DIF/99

######################################################

class EMU_MOD:

    def SIGMOID_M(self,v,a,d):
        return 1.0 / (1.0 + np.exp(-a * (v + d)))
    
    def SIGMOID_P(self,v,a,d):
        return 1.0 / (1.0 + np.exp(-a * (v - d)))
    
    def LAMBDA(self,v,old,a_m,a_p,d_m,d_p):
        return min(self.SIGMOID_M(v,a_m,d_m), max(old, self.SIGMOID_P(v,a_p,d_p)))

    def Lambert(self,x):
        #return np.log(1+x)*(1-np.log(1+np.log(1+x))/(2+np.log(1+x)))
        return lambertw(x)
    
    def I_nonlinear(self,V, I0, a, Rs):
        phi = a*Rs*I0
        return np.sign(V)*I0*(self.Lambert(phi*np.exp(a*np.abs(V)+phi))/phi-1)

    def hp(self,t, v, w = 0.5, mu = 1, Rc = 1000, lvl_on=0, lvl_off=99):
        w_debug = []
        
        lvl_diff = lvl_off-lvl_on;
           
        r_on = RES_MIN + lvl_on * QUANT_RES
        #v_off = 2.505;                  #Offset de voltaje
        #v_att = 0.6734;                 # Atenuación de voltaje
        #v_slope = 5.0 / 1023.0 / v_att; #
        #v_intercept = -v_off / v_att;   #
    
        #constante = mu * RES_MAX * 1.0e-9*v_slope;
        #mcp_correction = v_intercept/v_slope;

        R = [] 
        r_level = lvl_off - round(w*lvl_diff);
        R.append(RES_MIN+r_level*QUANT_RES);
        
        for i in range(len(t)-1):
            dt = t[i+1]-t[i]
            w = w + dt*mu*r_on*v[i]/(R[i]+Rc);
            # w = w + dt*constante*(mcp3008_read(0)+mcp_correction)/R[i];
            
            if (w<0):
                w = 0
            if (w>1):
                w = 1;
            w_debug.append(w)
            r_level = lvl_off - round(w*lvl_diff);
            
            R.append(RES_MIN+r_level*QUANT_RES);
        
        return np.array(R), np.array(w_debug)
    
    def histeron(self,t, v, w = 0.5, a_m = 1, a_p = 1, d_m = 1, d_p = 1, t0 = 1, v0 = 1, Rc = 1000, lvl_on=0, lvl_off=99):
        lvl_diff = lvl_off - lvl_on
    
    #    r_off = RES_MIN + QUANT_RES * lvl_off
    #    r_on = RES_MIN + QUANT_RES * lvl_on
    #    r_diff = QUANT_RES * lvl_diff
    
    #    v_off = 2.5 # Offset de voltaje
    #    v_att = 0.68 # Atenuación de voltaje
    #    v_slope = 5.0 / 1023.0 / v_att
    #    v_intercept = -v_off / v_att
        w_debug = []
        R = []
        r_level = lvl_off - round(w*lvl_diff)
        R.append(RES_MIN+r_level*QUANT_RES)
        lamb = self.SIGMOID_M(v[0], a_m, a_p, d_m, d_p)
    
        for i in range(len(t)-1):
            dt = t[i+1]-t[i]
            
            V = v[i]*R[i]/(R[i]+Rc)
            
            lamb = self.LAMBDA(V, lamb, a_m, a_p, d_m, d_p)
#           w += dt*(lamb - w) / (t0/np.exp(abs(V) / v0))
            w = (dt * lamb + (t0/np.exp(abs(V) / v0)) * w)/(dt + (t0/np.exp(abs(V) / v0)))
            
            if (w<0):
                w = 0
            elif (w>1):
                w = 1
            w_debug.append(w)
            r_level = lvl_off - round(w*lvl_diff)
            R.append(RES_MIN+r_level*QUANT_RES)
            
        return np.array(R), np.array(w_debug)

    def histeron_nonlinear(self,t, v, w = 0.5, eta_m = 1, eta_p = 1, delta_m = 1, delta_p = 1, t0 = 1, v0 = 1, alpha = 1, Rs = 100, I0min = 1, I0max = 1, Rc = 1000, Ron=30, Roff=10000):
        
        V_debug = []
        w_debug = []
        R_debug = []
        I_debug = []
        lamb_debug = []
        
        R = []
        R.append(Roff - round(w*(Roff-Ron)))
        lamb = self.SIGMOID_M(v[0], eta_m, delta_m)
    
        for i in range(len(t)-1):
            dt = t[i+1]-t[i]
            
            V = v[i]*R[i]/(R[i]+Rc)
            V_debug.append(V)
            lamb = self.LAMBDA(V, lamb, eta_m, eta_p, delta_m, delta_p)
            lamb_debug.append(lamb)
            w += dt*(lamb - w) / (t0/np.exp(abs(V) / v0))
#            w += dt*(lamb - w) / (t0)

            
            if (w<0):
                w = 0
            elif (w>1):
                w = 1
            
            w_debug.append(w)
            
            R_cur = V / self.I_nonlinear(V, I0min + w * (I0max - I0min), alpha, Rs)
            if R_cur < Ron:
              R_cur   = Ron
            if R_cur > Roff:
                R_cur = Roff
            
            R.append(R_cur)
            R_debug.append(R[i+1])
            I_debug.append(V/R[i+1])
            
        return np.array(R),w_debug,lamb_debug