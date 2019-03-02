import threading, time


class Timer(threading.Thread):
    def __init__(self,hora,minutos,segundos,contador):
        #Inicia el Hilo
        threading.Thread.__init__(self)
        self.hora = hora
        self.segundos = segundos
        self.minutos = minutos
        self.corriendo = False
        self.contador = contador

    def run(self):
        # Activa corr
        self.corriendo = True
        while True:
            for i in range(1,100):
                print "hola %d" %i
                time.sleep(1)
                if self.contador==0:
                    break
                else:
                    pass
            break

    def setStop(self):
        self.contador = 0


#Crea un Objeto timer
t1 = Timer("Hora 1:",5,50,2)

#Iniciamo el Thread
t1.start()

time.sleep(10)
t1.setStop()


