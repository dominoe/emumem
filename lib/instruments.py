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

    def set_instrument(self,wave,frec,amp):
        self.instrument.write(":APPL:%s %i,%.1f,0,0"%(wave,frec,amp))
        
    def set_output(self,CH,status):
        if status == 1:
            str_status = "ON"
        elif status == 0:
            str_status = "OFF"
        self.instrument.write(":OUTP {0}".format(str_status))

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

    def open_instrument(self,name):
        self.name = name
        self.resource = visa.ResourceManager()
        self.instrument = self.resource.open_resource(self.name)

    def get_value(self,s):
        return float(self.instrument.query(s))
    
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
    
    def get_channel(self,CH):
        self.instrument.write(':WAV:POIN:MODE MAX')
        self.instrument.write(':STOP')
        data = self.instrument.query_binary_values(':WAV:DATA? CHAN{0}'.format(CH), datatype='B', container=numpy.array)
        time = numpy.arange(len(data)) / self.get_s_rate() - self.get_t_offset()
        data = -(data - self.get_y_ref()) * self.get_y_inc(1) - self.get_v_offset(1)
        self.instrument.write(':RUN')
        return time, data

######################################################
