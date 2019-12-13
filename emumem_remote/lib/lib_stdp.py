# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 19:12:44 2019

@author: Compumar
"""
from time import sleep
import numpy as np
from scipy.signal import find_peaks
from scipy.signal import peak_widths
import matplotlib.pyplot as plt

#from scipy.signal import find_peaks

#%%############################################
## CONFIGURACIÓN DEL GENERADOR DE FUNCIONES
#
#gen_signal = emu_fun.custom_burst_signal(gen_signal_points,gen_signal_wait_probe,gen_signal_wait_spike,gen_signal_width_probe,gen_signal_width_spike,gen_signal_amp_probe,gen_signal_amp_spike)
#
#gen.set_instrument(gen_waveform,gen_frequency,gen_voltage,0.0,0.0)
#
#if (gen_waveform == 'CUST'):
#    gen.set_signal(gen_signal)
#
#gen.set_output(1)

#%%############################################
# ADQUISICIÓN DE PULSOS (REQUIERE PANTALLA EN STOP)

def acq_pulses (osc, gen, raspi_ssh, gen_frequency=2, gen_voltage=3, MODELO_NAME="hdp", MOD_PARAMS=[], first = False, burst_ncycles=10, gen_signal_amp_probe=0):
    
    #MOD_PARAMS:
    #           HP:     [w, mu, lvlon, lvloff, nmeds]
    #           HDP:    [w, alpha, delta, tau0, v0, lvlon, lvloff, nmeds]
    #           HDPN:   [w, eta, delta, tau0, v0, alpha, rs, i0min, i0max, lvlon, lvloff, nmeds]
    
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
        except:
            print("")

    t_scale = osc.get_t_scale()
    osc_time_1 = osc_time_2 = osc_data_1 = osc_data_2 = None
    
    while (osc_time_1 is None or osc_time_2 is None):
        # Se hace antes.
        gen.set_output(1)
        gen.burst_signal(1,burst_ncycles)
        gen.trig_source(1,"MANUAL")
        
    #    file_str = "data/STDP_modelo_" + MODELO_NAME + "_fr_" + str(gen_frequency) + "_volt_" + str(gen_voltage) + "_" + time.strftime("%Y%m%d-%H%M%S")
        
        if (MODELO_NAME == "hp"):
            raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hp {0} {1} {2} {3} {4} &'.format(MOD_PARAMS[0], MOD_PARAMS[1], MOD_PARAMS[2], MOD_PARAMS[3], MOD_PARAMS[4]))
        elif (MODELO_NAME == "hdp"):
            raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdp {0} {1} {2} {3} {4} {5} {6} {7} &'.format(MOD_PARAMS[0], MOD_PARAMS[1], MOD_PARAMS[2], MOD_PARAMS[3], MOD_PARAMS[4], MOD_PARAMS[5], MOD_PARAMS[6], MOD_PARAMS[7]))
        elif (MODELO_NAME == "hdpn"):
            raspi_ssh.execute_background('sudo nice -n-20 ./emumem/emumem modelo_hdpn {0} {1} {2} {3} {4} {5} {6} {7} {8} {9} {10} {11} &'.format(MOD_PARAMS[0], MOD_PARAMS[1], MOD_PARAMS[2], MOD_PARAMS[3], MOD_PARAMS[4], MOD_PARAMS[5], MOD_PARAMS[6], MOD_PARAMS[7], MOD_PARAMS[8], MOD_PARAMS[9], MOD_PARAMS[10], MOD_PARAMS[11]))
        
        raspi_ssh.wait(5) # Cambié de 10 a 5.
        
        try:
            osc.single()
        except:
            print("")
        
        sleep(5)
        gen.trigger()
        
        sleep(t_scale*15)
        
        try:
            osc_time_1, osc_data_1 = osc.get_channel(1)
        except:
            print("")
        try:
            osc_time_2, osc_data_2 = osc.get_channel(2)
        except:
            print("")
        
        raspi_ssh.kill_instances('emumem')
        gen.burst_off(1)
        sleep(5)
    return (osc_time_1, osc_data_1, osc_time_2, osc_data_2)
    
#plt.figure(1)
#plt.clf()
#plt.plot(osc_time_1, osc_data_1)
#plt.plot(osc_time_2, osc_data_2)
#
#plt.xlabel('Tiempo (s)')
#plt.ylabel('Tensión (V)')

#%%############################################
# DETECCIÓN Y MEDICIÓN DE PROBES DEL GENERADOR
def process_pulses (t, v, vmem, Rc, est_voltage, est_width, freq=2, n_cycles=10, tolerance_min=0.2, tolerance_max=0.2, tolerance_width=0.1):
#    est_voltage_spike = gen_voltage*gen_signal_amp_spike/2
#    est_voltage_probe  = (gen_voltage/2)*gen_signal_amp_probe
    
#    tolerance_spike = 0.1
#    tolerance_probe = 0.2
    
#    max_voltage_spike = est_voltage_spike*(1.0+tolerance_spike)
#    min_voltage_spike = est_voltage_spike*(1.0-tolerance_spike)
    
    i = (v - vmem) / Rc
    
    num_meds = len(t)
    period = 1/freq
    acq_time = max(t)-min(t)
    points_in_period = int(round(num_meds*(period/acq_time))) # Se usa para mejorar la búsqueda de probes, así busca uno solo por periodo.
    
    max_voltage = est_voltage*(1.0+tolerance_max)
    min_voltage = est_voltage*(1.0-tolerance_min)
    
    tolerance_width = 0.1

    est_width = points_in_period*est_width/100
    
    max_width = est_width*(1.0+tolerance_width)
    min_width = est_width*(1.0-tolerance_width)
    
    peak_probes,_ = find_peaks(v,height=(min_voltage,max_voltage),distance=points_in_period*0.95,width=(min_width,max_width))
    width_probes = peak_widths(v, peak_probes, rel_height=0.2)

    #plt.plot(range(len(v)),v,end_probes,v[end_probes],'.')
    
    if not (len(peak_probes) == n_cycles):
        print("Hubo un problema en la búsqueda de picos, intentar de nuevo (" + str(len(peak_probes)) + " hallados, " + str(n_cycles) + " esperados).")
        return None
    
#    plt.figure("pulsos")
#    plt.clf()
#    plt.xlabel("Tiempo (s)")
#    plt.ylabel("Tensión (V)")
#    plt.plot(t,v,t,vmem)
    
    v_mean = np.empty(0)
    v_se = np.empty(0)
    vmem_mean = np.empty(0)
    vmem_se = np.empty(0)
    i_mean = np.empty(0)
    i_se = np.empty(0)
    
    for c in range(n_cycles):
#        plt.plot(t,vmem)
#        plt.plot(t[int(width_probes[2][c])+1:int(width_probes[3][c])],vmem[int(width_probes[2][c])+1:int(width_probes[3][c])],'.')
        v_mean = np.append(v_mean, np.mean(v[int(width_probes[2][c])+1:int(width_probes[3][c])]))
        v_se = np.append(v_se, np.std(v[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))
        vmem_mean = np.append(vmem_mean, np.mean(vmem[int(width_probes[2][c])+1:int(width_probes[3][c])]))
        vmem_se = np.append(vmem_se, np.std(vmem[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))
        i_mean = np.append(i_mean, np.mean(i[int(width_probes[2][c])+1:int(width_probes[3][c])]))
        i_se = np.append(i_se, np.std(i[int(width_probes[2][c])+1:int(width_probes[3][c])])/np.sqrt(np.round(points_in_period*0.05)))
    
    r_mean = vmem_mean/i_mean
    r_se = r_mean * np.sqrt((vmem_se/vmem_mean)**2+(i_se/i_mean)**2)

    plt.figure("Resistencias")
    plt.clf()
    plt.errorbar (range(n_cycles), r_mean, r_se, fmt='o')
    plt.xlabel("Pulso")
    plt.ylabel("Resistencia ($\Omega$)")
    
    return (r_mean, r_se)
