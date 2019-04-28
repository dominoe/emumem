from lib.instruments import *

from matplotlib import pyplot as plt

######################################################

# PLOT FOR ONE RESISTANCE

gen = RIGOL_DG4162();
gen.open_instrument('USB0::0x1AB1::0x0641::DG4C150400092::INSTR')
gen.set_instrument('SIN',1000,2.0)

raspi_ssh = RASPBERRY_PI2_SSH()
raspi_ssh.connect('10.2.40.31',22,'pi','memristorpi')
raspi_ssh_stdout = raspi_ssh.execute('cd Documents/emu_mem/ \n sudo ./main "set" 6000')
raspi_ssh.wait(1)
print(raspi_ssh_stdout)

osc = RIGOL_DS1204B();
osc.open_instrument('USB0::0x1AB1::0x0488::DS1BA113200430::INSTR')
osc_time_1, osc_data_1 = osc.get_channel(1)
osc_time_2, osc_data_2 = osc.get_channel(2)

plt.clf()
plt.plot(osc_time_1, osc_data_1, osc_time_2, osc_data_2)
plt.xlabel('Tiempo [s]')
plt.ylabel('Voltaje [V]')

######################################################

#raspi_ssh_stdout = raspi_ssh.execute('cd Documents/emu_mem/ \n sudo ./main {0}'.format(i*100))

Vpot = osc.get_vrms(1)
Vgen = osc.get_vrms(2)

print(Vpot)

r_l = 1000
r_t = 10000
r_reos = 1000/(Vgen/Vpot-1)
r_div = Vpot/Vgen*(r_l+r_t)

print(r_div)