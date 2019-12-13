######################################################
### ULTIMA MODIFICACIÓN: 2019-06-27
######################################################

import visa, paramiko, numpy
from time import sleep

######################################################

class RASPBERRY_PI2_SSH:

    hostname = None
    port = None
    username = None
    password = None
    ssh_client = None
    command = None
    
    def connect(self,hostname,port,username,password):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.load_system_host_keys()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh_client.connect(hostname, port=port, username=username, password=password)

    def execute(self,command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        tmp = stdout.readlines()
        return ''.join(tmp)

    def execute_background(self,command):
        self.ssh_client.exec_command(command)

    def get_pids(self,name):
        return self.execute('sudo ps -x | grep -e "{}"'.format(name)  + ' | awk \'{print $1}\'').splitlines()

    def kill_instances(self,name):
        self.execute_background('sudo kill $(sudo ps -x | grep -e "{}"'.format(name) + ' | awk \'{print $1}\')')
        
    def wait(self,time):
        sleep(time)

######################################################

class RIGOL_DG4162:

    name = None
    resource = None
    instrument = None
    # wave: CUST, HARM, NOI, PULS, RAMP, SIN, SQU, USER

    def open_instrument(self,name):
        self.name = name
        self.resource = visa.ResourceManager()
        self.instrument = self.resource.open_resource(self.name)

    def set_instrument(self,wave,frequency,amplitude=0.0,offset=0.0,phase=0.0,channel=1):
        self.instrument.write(":SOUR%d:APPL:%s %.1f,%.1f,%.1f,%.1f"%(channel,wave,frequency,amplitude,offset,phase))

    def set_signal(self,signal,channel=1):
        self.instrument.write("SOUR{0}:TRAC:DATA VOLATILE ".format(channel) + ',' +  ','.join(map(str, signal[0,:])))
        self.instrument.write("SOUR{0}:TRAC:DATA:POINts:INTerpolate OFF".format(channel))

    def burst_signal(self,channel,cycles):
        self.instrument.write(":SOUR{0}:BURS:NCYC {1}".format(channel,cycles))
        self.instrument.write(":SOUR{0}:BURS ON".format(channel))
        print("BURST")
    
    def burst_off(self,channel):
        self.instrument.write(":SOUR{0}:BURS OFF".format(channel))
    
    def trig_source(self, channel, src):
        self.instrument.write(":SOUR{0}:BURS:TRIG:SOUR {1}".format(channel,src))
    
    def trig_slope(self, channel, slope):
        self.instrument.write(":SOUR{0}:BURS:TRIG:SLOP {1}".format(channel,slope))
    
    def trigger(self):
        print ("Gen triggered")
        self.instrument.write("*TRG")

    def set_output(self,status,channel=1):
        if status == 1:
            str_status = "ON"
        elif status == 0:
            str_status = "OFF"
        self.instrument.write(":OUTP{0} {1}".format(channel,str_status))

######################################################

class RIGOL_DS1204B:

    name = None
    resource = None
    instrument = None
    v_scale = None
    v_offset = None
    t_scale = None
    t_offset = None
    s_rate = None
    y_ref = None
    y_inc = None
    
    t_scale_list = [list(numpy.array([1,2,5])*10**(i)) for i in range(-9,2)]
    
    def open_instrument(self,name):
        self.name = name
        self.resource = visa.ResourceManager()
        self.instrument = self.resource.open_resource(self.name)
    
    def run(self):
        self.instrument.query(':RUN')
    
    def stop(self):
        self.instrument.query(':STOP')
        
    def single(self):
        self.instrument.query(':SINGLE')

    def set_value(self,s):
        self.instrument.query(s)

    def get_value(self,s):
        return float(self.instrument.query(s))

    def set_t_scale(self,SCALE):
        self.set_value(':TIM:SCAL {0}'.format(SCALE))

    def set_v_scale(self,CH,SCALE):
        self.set_value(':CHAN{0}:SCAL {1}'.format(CH,SCALE))
        
    def set_t_offset(self,OFFSET):
        self.set_value(':TIM:OFFS {0}'.format(OFFSET))
    
    def set_v_offset(self,CH,OFFSET):
        self.set_value('CHAN{0}:OFFS {1}'.format(CH,OFFSET))

    def set_trig_lvl(self,LEVEL):
        self.set_value(':TRIG:EDGE:LEV {0}'.format(LEVEL))

    def get_v_scale(self,CH):
        return self.get_value(':CHAN{0}:SCAL?'.format(CH))

    def get_v_offset(self,CH):
        return self.get_value(':CHAN{0}:OFFS?'.format(CH))

    def get_t_scale(self):
        return self.get_value(':TIM:SCAL?')

    def get_t_offset(self):
        return self.get_value(':TIM:OFFS?')

    def get_s_rate(self):
        return self.get_value(':ACQ:SRAT?')

    def get_y_ref(self):
        tmp = self.instrument.query(':WAV:PRE?')
        tmp = tmp.split(',')
        return float(tmp[9])

    def get_y_inc(self,CH):
        return self.get_value(':WAV:YINC? CHAN{0}'.format(CH))
    
    def get_vrms(self,CH):
        return self.get_value(':MEAS:VRMS? CHAN{0}'.format(CH))

    def get_vmax(self,CH):
        return self.get_value(':MEAS:VMAX? CHAN{0}'.format(CH))

    def get_vmin(self,CH):
        return self.get_value(':MEAS:VMIN? CHAN{0}'.format(CH))

    def get_vmean(self,CH):
        return self.get_value(':MEAS:VAV? CHAN{0}'.format(CH))
    
    def get_sample_rate(self,CH):
        return self.get_value(':ACQ:SRAT? CHAN{0}'.format(CH))
    
    def get_channel(self,CH):
        self.instrument.write(':WAV:POIN:MODE MAX')
#        self.instrument.write(':STOP')
        data = self.instrument.query_binary_values(':WAV:DATA? CHAN{0}'.format(CH), datatype='B', container=numpy.array)
        time = numpy.arange(len(data)) / self.get_s_rate() - self.get_t_offset()
        data = -(data - self.get_y_ref()) * self.get_y_inc(CH) - self.get_v_offset(CH)
#        self.instrument.write(':RUN')
        return time, data
    
    def get_trig_lvl(self):
        self.get_value(':TRIG:EDGE:LEV?')

######################################################