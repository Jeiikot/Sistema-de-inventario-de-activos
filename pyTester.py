import serial
import threading

class sensor:
    def __init__(self,puerto,laboratorio):
        self.laboratorio = laboratorio
        puertoSerial = serial.Serial(
            port=puerto,
            baudrate =9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=1)
        print("Iniciando...")
        print("connected to: " + puertoSerial.portstr + " " + str(puertoSerial.baudrate))
        while True:
            Lectura=""
            if (puertoSerial.inWaiting()>0):
                Lectura+=puertoSerial.read(12)
                if len(Lectura)==3:
                    UID= Lectura.encode("hex")
                    print UID + " " + self.laboratorio


s1 = threading.Thread(target= sensor, args=("/dev/ttyUSB0","Laboratorio 1",))
#s2 = threading.Thread(target= sensor, args=("/dev/ttyUSB1","Laboratorio 2",))

s1.start()
#s2.start()
