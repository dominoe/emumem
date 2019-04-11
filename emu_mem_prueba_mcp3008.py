from lib.instruments import *

from matplotlib import pyplot as plt

import csv

gen = RIGOL_DG4162()
gen.open_instrument('USB0::0x1AB1::0x0641::DG4C150400092::INSTR')
raspi_ssh = RASPBERRY_PI2_SSH()
raspi_ssh.connect('10.2.40.31',22,'pi','memristorpi')
osc = RIGOL_DS1204B();
osc.open_instrument('USB0::0x1AB1::0x0488::DS1BA113200430::INSTR')

#gen.set_instrument('SIN',1000,5.0)
#gen.set_output(1,1)

v_ref = 5

f = 50 # En ksps
t = 1  # En milisegundos
ch = 0
tot_meds = t*f
adq_mcp = raspi_ssh.execute('cd Documents/emumem/ \n sudo ./main adq_mcp {0} {1} {2}'.format(f, t, ch)).splitlines()
res = []

t_cnt = 0

for i, line in enumerate(adq_mcp):
    res.append(line.split("\t"))
    res[i][0] = int(res[i][0])
    res[i][1] = int(res[i][1])
    if i > 0:
        d_t = res[i][0] - (res[i-1][0] - t_cnt)*10**9
        if (d_t < 0):
            t_cnt += 1
    res[i][0] = float(res[i][0]*10**(-9)) + t_cnt
            
res = numpy.array(res)

res[:,0] = res[:,0] - res[:,0][0]
res[:,1] = res[:,1]/1023 * v_ref

with open('prueba.csv', 'w') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerows(res)
csvFile.close()

plt.clf()
plt.plot(res[:,0], res[:,1], '-')
plt.ylabel('Voltaje [V]')
plt.xlabel('Tiempo [s]')