"""
Utilizando una distribución exponencial

@author: Pablo Sao
@author: Amado García
@date: 22-02-2019
"""
#Importando Librerias
import simpy
import random

#Creación de variables
interval = 10
RAM = 100 #Capacidad de memoria RAM
number = random.expovariate(1.0 / interval)
CPU = 1 #unidad de tiempo
procesos = 25 #procesos a realizar



def proceso(nombre, env, interval, cpu,ram):

    global totalDia  # :( mala practica, pero ni modo

    # Simular que esta conduciendo un tiempo antes de llegar a la gasolinera
    yield env.timeout(interval)

    # llegando a la gasolinera
    horaLlegada = env.now

    # simular que necesita un tiempo para cargar gasolina. Probablemente
    # si es carro pequeño necesita menos tiempo y si es carro grande mas tiempo
    tiempoGas = random.randint(1, 7)
    print('%s inicia a las %f nececita %d para completar el proceso' % (nombre, horaLlegada, tiempoGas))

    # ahora se dirige a la bomba de gasolina,
    # pero si hay otros carros, debe hacer cola
    with cpu.request() as turno:
        with ram.request() as turno2:
            yield turno  # ya puso la manguera de gasolina en el carro!
            yield env.timeout(tiempoGas)  # hecha gasolina por un tiempo
            print('%s sale del proceso a las %f' % (nombre, env.now))
            # aqui el carro hace un release automatico de la bomba de gasolina

    tiempoTotal = env.now - horaLlegada
    print('%s se tardo %f' % (nombre, tiempoTotal))
    totalDia = totalDia + tiempoTotal


# ----------------------

env = simpy.Environment()  #ambiente de simulación
cpu_resource = simpy.Resource(env, capacity=CPU) # CPU a tulizar

totalDia = 0
for i in range(5):
    env.process(proceso('Proceso %d' % i, env, number, cpu_resource,RAM))

env.run(until=procesos)  # correr la simulación hasta el tiempo = 50

print("tiempo promedio del proceso es: ", totalDia / 5.0)
