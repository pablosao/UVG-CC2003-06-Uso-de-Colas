#!/usr/bin/env python
# coding: utf-8

# In[171]:


import simpy
import random
import graficas
from random import seed
seed(123)
  
def Process(name, env,  cpu, ram):
    global tiempoPromedio
    tempRam = random.randint(1,10)
    instructions = random.randint(1,10)
    yield env.timeout(random.expovariate(1.0/1)) #Generates new Process
    
    #Ram ------------------------------
    with RAM.get(tempRam) as queueForRam:
        yield queueForRam
        print('Process %s is in new state at %s' % (name, env.now))
        print('Process %s requested %s of RAM' % (name, tempRam))
        ramProcess = tempRam
        print(RAM.level,"RAM available")

        #CPU ---------
        yield env.timeout(0.5)
        print('Process %s is in Ready mode at %s' % (name, env.now))
        print('Process %s requested the CPU' %(name))
        print('Process %s has %s instructions' %(name, instructions))
        while(instructions > 0):
            with CPU.request() as req:
                yield req
                print('Process %s is running now' % (name))
                if((instructions - 3) <= 0): ##change this if wanna change the instructions per Process
                    yield env.timeout((1/instructions) * instructions)
                    instructions = instructions - instructions
                    print('Process %s is Terminated at %s' %(name, env.now))
                    tiempoPromedio = env.now
                    listCPU.append(env.now)
                    RAM.put(ramProcess) 
                else:
                    yield env.timeout(1)
                    instructions = instructions - 3 ##change this if wanna change the instructions per Process
                    print('Process %s leaves the CPU at %s' % (name, env.now))
                    io = random.randint(1,2)
                    if io == 1:
                        print('Process %s is in waiting state' % (name))
                        yield env.timeout(1)
                    else:
                        print('Process %s is in ready state' % (name))
                        print('Process %s has %s instructions left' % (name, instructions ))
        
        
#Simpy enviroment 
env = simpy.Environment()
CPU = simpy.Resource(env, capacity=1)
RAM = simpy.Container(env, init=100, capacity=100)
ramProcess = 0
instructions = 0
listCPU = list()
tiempoPromedio = 0
process_Quantity = 25

#New Processes
for i in range(process_Quantity):
    env.process(Process(i, env, CPU, RAM))
    
env.run()

#Data
tiempoPromedio = tiempoPromedio / process_Quantity
print("El tiempo promedio ", tiempoPromedio)


desvest = tiempoPromedio / process_Quantity

print("Desviacion estandar: ", desvest)

#Graphics generator
graficas.plotear(process_Quantity, listCPU, "CPU")






# 

# In[ ]:





# In[ ]:




