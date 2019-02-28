'''

@author: Pablo Sao
@author: Amado García
@date: 22-02-2019
'''


#Importando Librerias
import simpy
import random
import graficas

#Creación de variables
INTERVALO = 10
RAM = 100 #Capacidad de memoria RAM
CPU = 1 #unidad de tiempo
PROCESOS = 25 #procesos a realizar

#Variables que cambiaran durante el tiempo de ejecución

totalProcesos = 0
counter = 0


#Listas para ploteo de graficas
pro = list()  #lista de procesos
cpuTime = list() #lista que contiene el tiempo de cpu
ramTime = list() #lista que contiene el tiempo de ram



def proceso(nombre, env, interval, cpu,ram):
    '''

    :param nombre:
    :param env:
    :param interval:
    :param cpu:
    :param ram:
    :return:
    '''

    global totalDia  # :( mala practica, pero ni modo\
    global counter
    global totalProcesos

    # Simular que esta conduciendo un tiempo antes de llegar a la gasolinera
    yield env.timeout(interval)

    # llegando a la gasolinera
    horaLlegada = env.now

    # Variables para simular el tiempo que tarda en realizar un proceso la CPU y la RAM
    tiempoCPU = random.randint(1, 3)
    tiempoRam = random.randint(1, 5)
   
   
    # Iniciamos el proceso del CPU, si ya esta ocupado por otro proceso, espera hasta ser liberado
    with cpu.request() as turno_cpu:
        yield turno_cpu  # ya puso la manguera de gasolina en el carro!
        yield env.timeout(tiempoCPU)  # hecha gasolina por un tiempo
        try:
            # Iniciamos el proceso de la RAM si ya esta ocupado por otro proceso, espera hasta ser liberado
            with ram.request() as turno_ram:
                yield turno_ram
                yield env.timeout(tiempoRam)
          
                print('%s inicia a las %f necesita %d para Ingresar al cpu' % (nombre, horaLlegada, tiempoCPU))
                print('%s continua a las %f necesita %d para completar el proceso' % (nombre, horaLlegada + tiempoCPU, tiempoRam))
                print('%s sale del proceso a las %f' % (nombre, env.now))
                

        except Exception:
            print(Exception)
   
    tiempoTotal = env.now - horaLlegada
    print('%s se tardo %f' % (nombre, tiempoCPU + tiempoRam))
    totalProcesos = totalProcesos + tiempoTotal
    pro.append(counter)
    cpuTime.append(tiempoCPU)
    ramTime.append(tiempoRam)
    counter = counter + 1
    


# ----------------------

env = simpy.Environment()  #ambiente de simulación
cpu_resource = simpy.Resource(env, capacity=CPU) # ambiente del CPU a tulizar
ram_resource = simpy.Resource(env, capacity=RAM) # ambiente de la RAM a tulizar

for i in range(25):
    proc = env.process(proceso('Proceso %d' % i, env, random.expovariate(1.0 / INTERVALO), cpu_resource,ram_resource))

env.run()

proceso = round(totalProcesos / PROCESOS,2)

print("tiempo promedio del proceso es: ", proceso)



#graficas.plotear(proceso,pro)
graficas.plotear(proceso,cpuTime,"CPU",ramTime,"RAM")
