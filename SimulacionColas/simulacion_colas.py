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
number = random.expovariate(1.0 / interval)
RAM = 100 #Capacidad de memoria RAM
CPU = 1 #unidad de tiempo
procesos = 25 #procesos a realizar
