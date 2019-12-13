######################################################
### ULTIMA MODIFICACIÓN: 2019-06-27
######################################################

import numpy as np

######################################################

class EMU_FUN:

    def custom_burst_signal(self,gen_signal_points, gen_signal_wait_probe, gen_signal_wait_spike, gen_signal_width_probe, gen_signal_width_spike, gen_signal_amp_probe, gen_signal_amp_spike):
        n0 = int(gen_signal_wait_probe/100*gen_signal_points)
        n1 = int(gen_signal_width_spike/100*gen_signal_points)
        n2 = int(gen_signal_wait_spike/100*gen_signal_points)
        n3 = int(gen_signal_width_probe/100*gen_signal_points)
        #gen_signal = np.zeros((1,gen_signal_points))
        #gen_signal[0,2*n1:3*n1] = gen_signal_amp_spike
        #gen_signal = gen_signal-np.roll(gen_signal,n2,axis = 1)
        #gen_signal[0,2*n1-n0-n3:2*n1-n0] = gen_signal_amp_probe
        #gen_signal[0,3*n1+n2+n0:3*n1+n2+n0+n3] = gen_signal_amp_probe
        gen_signal = np.zeros((1,gen_signal_points))
        gen_signal[0,n0+n3:n0+n3+n1] = gen_signal_amp_spike
        gen_signal = gen_signal-np.roll(gen_signal,n2,axis = 1)
        gen_signal[0,0] = 0
        gen_signal[0,1:n3] = gen_signal_amp_probe
        return gen_signal
    
    def gen_pavlov_bell (self, gen_signal_points, gen_duty_cycle, gen_signal_amp, pulse_freq, tot_time, test_pulse_train_size):
        num_periods = tot_time * pulse_freq
        test_periods = test_pulse_train_size * 3
        pulse_points = int(gen_signal_points / num_periods)
        n0 = int(gen_duty_cycle*pulse_points)
        zero_signal = np.zeros(pulse_points)
        pulse_signal = np.zeros(pulse_points)
        pulse_signal[1:n0+1] = gen_signal_amp
        
        bell_signal = np.tile(pulse_signal,test_pulse_train_size)
        bell_signal = np.concatenate((bell_signal,np.tile(zero_signal,test_pulse_train_size)))
        bell_signal = np.concatenate((bell_signal,np.tile(pulse_signal,int(num_periods - 2/3*test_periods))))
        
        return bell_signal
    
    def gen_pavlov_food (self, gen_signal_points, gen_duty_cycle, gen_signal_amp, pulse_freq, tot_time, test_pulse_train_size):
        num_periods = tot_time * pulse_freq
        pulse_points = int(gen_signal_points / num_periods)
        n0 = int(gen_duty_cycle*pulse_points)
        zero_signal = np.zeros(pulse_points)
        pulse_signal = np.zeros(pulse_points)
        pulse_signal[1:n0+1] = gen_signal_amp
        
        food_signal = np.tile(zero_signal, test_pulse_train_size)
        food_signal = np.concatenate((food_signal,np.tile(pulse_signal,test_pulse_train_size)))
        food_signal = np.concatenate((food_signal,np.tile(zero_signal,test_pulse_train_size)))
        food_signal = np.concatenate((food_signal,np.tile(pulse_signal,test_pulse_train_size)))
        food_signal = np.concatenate((food_signal,np.tile(zero_signal,test_pulse_train_size*2)))
        food_signal = np.concatenate((food_signal,np.tile(pulse_signal,test_pulse_train_size)))
        food_signal = np.concatenate((food_signal,np.tile(zero_signal,int(num_periods - 7*test_pulse_train_size))))
        
        return food_signal