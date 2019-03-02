import serial

#serialPort.baudrate = 19200
#serialPort.port = 'COM1'
#print serialPort.portstr
#print serialPort
#print serialPort.is_open

serialPort = serial.Serial(
    port = "/dev/ttyUSB0",
    baudrate =9600,
    parity = serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )


try:
    print serialPort.is_open
    print serialPort.isOpen()
    print "Serial port is open"

except IOError:
    print('An error occured trying to read the file.')

except ValueError:
    print('Non-numeric data found in the file.')

except ImportError:
    print "NO module found"

except EOFError:
    print('Why did you do an EOF on me?')

except KeyboardInterrupt:
    print('You cancelled the operation.')
except:
    print "Error"
    exit()

if (serialPort.isOpen()):
    try:
        while(True):
            print serialPort.read().encode("hex")
    except Exception:
        print "Error 2"
else:
    print "No se puede abrir el puerto serial"

