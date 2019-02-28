#!/usr/bin/env python
# coding: utf-8

# In[50]:


import simpy
import random
from random import seed
seed(123)
  
#Generates the process
def process_Generator(env):
    for i in range(process_Quantity):
        yield env.timeout(random.expovariate(1.0 / 10))
        env.process(ram_Request(i, env))
        env.process(cpu_Request(i, env))

#Ask for RAM
def ram_Request(name, env):
    global instructions
    global ramProcess
    instructions.insert(int(name), random.randint(1,10))
    print('Process %s is in new state at %s' % (name, env.now))
    print('Process %s requested the RAM' % (name))
    if RAM.level < instructions[name]:
        print("Proces %s requires %s ram space, but there's only %s RAM available, getting back to queue" %(name, instructions[name], RAM.level))
        cpu_Queue.insert(len(cpu_Queue) - 1, cpu_Queue)
    else:
        tempRam = RAM.get(random.randint(1,10))
        yield tempRam
        ramProcess.insert(int(name), tempRam)
        print(RAM.level,"RAM available")
    
        
#Asks for CPU disponibility
def cpu_Request(name, env):
    global cpu_Queue

    yield env.timeout(0.5)
    print('Process %s is in Ready mode at %s' % (name, env.now))
    print('Process %s requested the CPU' %(name))
    print('Process %s has %s instructions' %(name, instructions[int(name)]))
    with CPU.request() as req:
        print('Procesos en cola: %s' % (len(cpu_Queue)))
        cpu_Queue.insert(0,name)
        yield req
        print('Process %s is running now' % (name))
        if(instructions[name] - 3 <= 0):
            yield env.timeout(instructions[name])
        else:
            yield env.timeout(1) 
            cpu_Queue.insert(0,name)
        print('Process %s leaves the CPU at %s' % (name, env.now))
        del cpu_Queue[len(cpu_Queue) - 1]
        instructions[int(name)] = instructions[int(name)]- 3
        print('Process %s has %s instructions left' % (name, instructions[int(name)] ))       
        
        
#Simpy enviroment 
env = simpy.Environment()
CPU = simpy.Resource(env, capacity=1)
RAM = simpy.Container(env, init=100, capacity=100)
cpu_Queue = []
instructions = []
ramProcess = []
process_Quantity = 25
process_gen = env.process(process_Generator(env))
env.run()


 
#How Ram works
#The process has to enqueue to request the necessary memory 
#It stays in the queu until it gets this quantity 
#When the process is done, it returns the memory amount used

#CPU
#1 process at 1 Unit time, which can do 3 instructions at a time 
#(*env.timeout())
#Gotta use Resource


#env = simpy.Environment()
#RAM = simpy.Container(env, init=RAM_CAPACITY, capacity=RAM_CAPACITY)
#CPU = simpy.Resource(env, capacity=CPU)

#States of the process 
#New -> Goes to the RAM to be assigned a variable quantiy of it (Random number from 1 to 10)
##If there's enough memory, it changes to "Ready", otherwise it'll be enqueue until it is enough memory 


    
        
#Ready -> Process is ready but it must wait to get to the CPU. The process has a counter with the quantity of 
##Total instructions to do(random numbers from 1 to 10). Whhen CPU is not used, the process can get to it. 

#Running -> CPU takes a process for a limited time, enough to get along with 3 instructions. 
#after that the process gets out of the CPU. The instructions counter of the process will go down by 3. If the process
#has less than 3 instructions left, it gets out of the CPU earlier 


#After CPU
#a) Terminated: If the process has no instructions left it leaves  the system and change its state to terminated. 
#b) Waiting: Generates a random number from 1 to 2. if 1 then goes to waiting queue to do I/O. When it leaves the queue
#it changes to Ready

#c) if the number is 2, it changes to ready queue 







# 
