from lib.instruments import *

from matplotlib import pyplot as plt

gen = RIGOL_DG4162()
gen.open_instrument('USB0::0x1AB1::0x0641::DG4C150400092::INSTR')
raspi_ssh = RASPBERRY_PI2_SSH()
raspi_ssh.connect('10.2.40.31',22,'pi','memristorpi')
osc = RIGOL_DS1204B();
osc.open_instrument('USB0::0x1AB1::0x0488::DS1BA113200430::INSTR')

gen.set_instrument('SIN',1000,3.0)
gen.set_output(1,1)


vg = osc.get_vrms(2)
vw = []
dv = 4 / 2**8
dw = []
rl = 1000
rp = 10000
rt = rp+rl
rw_div = []
rw_reo = []
N = 8000

raspi_ssh.execute('cd Documents/emu_mem/ \n sudo ./main "reset"')

for i in range(100):
    raspi_ssh.execute('cd Documents/emu_mem/ \n sudo ./main "inc" 1')
    vw.append( osc.get_vrms(1) )
    rw_div.append( vw[i] * rt/vg )
    rw_reo.append( rl / (vg/vw[i]-1) )
     
dw = numpy.array(vw)/numpy.sqrt(N)
#dr = numpy.array(rw)/numpy.sqrt(N)

plt.clf()
plt.errorbar(vw, rw_reo, xerr=dw, fmt='.')
plt.ylabel('Resistencia  [Ohm]')
plt.xlabel('Tensión [V]')