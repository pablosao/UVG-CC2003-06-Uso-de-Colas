{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "###  @author: Pablo Sao\n",
    "### @author: Amado García\n",
    "### @date: 22-02-2019\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Proceso 3 inicia a las 1.500089 necesita 3 para Ingresar al cpu\n",
      "Proceso 3 continua a las 4.500089 necesita 4 para completar el proceso\n",
      "Proceso 3 sale del proceso a las 8.500089\n",
      "Proceso 3 se tardo 7.000000\n",
      "Proceso 0 inicia a las 9.370607 necesita 2 para Ingresar al cpu\n",
      "Proceso 0 continua a las 11.370607 necesita 3 para completar el proceso\n",
      "Proceso 0 sale del proceso a las 14.370607\n",
      "Proceso 0 se tardo 5.000000\n",
      "Proceso 2 inicia a las 16.070688 necesita 3 para Ingresar al cpu\n",
      "Proceso 2 continua a las 19.070688 necesita 4 para completar el proceso\n",
      "Proceso 2 sale del proceso a las 23.070688\n",
      "Proceso 2 se tardo 7.000000\n",
      "tiempo promedio del proceso es:  0.76\n"
     ]
    }
   ],
   "source": [
    "\n",
    "#Importando Librerias\n",
    "import simpy\n",
    "import random\n",
    "\n",
    "#Creación de variables\n",
    "interval = 10\n",
    "RAM = 100 #Capacidad de memoria RAM\n",
    "CPU = 1 #unidad de tiempo\n",
    "procesos = 25 #procesos a realizar\n",
    "\n",
    "\n",
    "\n",
    "def proceso(nombre, env, interval, cpu,ram):\n",
    "\n",
    "    global totalDia  # :( mala practica, pero ni modo\n",
    "    # Simular que esta conduciendo un tiempo antes de llegar a la gasolinera\n",
    "    yield env.timeout(interval)\n",
    "\n",
    "    # llegando a la gasolinera\n",
    "    horaLlegada = env.now\n",
    "\n",
    "    # simular que necesita un tiempo para cargar gasolina. Probablemente\n",
    "    # si es carro pequeño necesita menos tiempo y si es carro grande mas tiempo\n",
    "    tiempoCPU = random.randint(1, 3)\n",
    "    tiempoRam = random.randint(1,5)\n",
    "   \n",
    "   \n",
    "    # ahora se dirige a la bomba de gasolina,\n",
    "    # pero si hay otros carros, debe hacer cola\n",
    "    with cpu.request() as turno_cpu:\n",
    "        yield turno_cpu  # ya puso la manguera de gasolina en el carro!\n",
    "        yield env.timeout(tiempoCPU)  # hecha gasolina por un tiempo\n",
    "        try:\n",
    "\n",
    "            with ram.request() as turno_ram:\n",
    "                yield turno_ram\n",
    "                yield env.timeout(tiempoRam)\n",
    "                print('%s inicia a las %f necesita %d para Ingresar al cpu' % (nombre, horaLlegada, tiempoCPU))\n",
    "                print('%s continua a las %f necesita %d para completar el proceso' % (nombre, horaLlegada + tiempoCPU, tiempoRam))\n",
    "                print('%s sale del proceso a las %f' % (nombre, env.now))\n",
    "                \n",
    "\n",
    "        except Exception:\n",
    "            print(Exception)\n",
    "    tiempoTotal = env.now - horaLlegada\n",
    "    print('%s se tardo %f' % (nombre, tiempoTotal))\n",
    "    totalDia = totalDia + tiempoTotal\n",
    "    \n",
    "\n",
    "\n",
    "# ----------------------\n",
    "\n",
    "env = simpy.Environment()  #ambiente de simulación\n",
    "cpu_resource = simpy.Resource(env, capacity=CPU) # CPU a tulizar\n",
    "ram_resource = simpy.Resource(env, capacity=RAM) # RAM a tulizar\n",
    "totalDia = 0\n",
    "\n",
    "for i in range(5):\n",
    "    env.process(proceso('Proceso %d' % i, env, random.expovariate(1.0 / 10), cpu_resource,ram_resource))\n",
    "\n",
    "env.run(until=procesos)  # correr la simulación hasta el tiempo = 50\n",
    "\n",
    "print(\"tiempo promedio del proceso es: \", totalDia / procesos)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "carro 3 llega a las 2.307955 necesita 7 para hechar gasolina\n",
      "carro 1 llega a las 5.601718 necesita 3 para hechar gasolina\n",
      "carro 0 llega a las 8.472372 necesita 6 para hechar gasolina\n",
      "carro 2 llega a las 8.629663 necesita 7 para hechar gasolina\n",
      "carro 3 sale de gasolinera a las 9.307955\n",
      "carro 3 se tardo 7.000000\n",
      "carro 1 sale de gasolinera a las 12.307955\n",
      "carro 1 se tardo 6.706238\n",
      "carro 4 llega a las 16.783661 necesita 2 para hechar gasolina\n",
      "carro 0 sale de gasolinera a las 18.307955\n",
      "carro 0 se tardo 9.835583\n",
      "carro 2 sale de gasolinera a las 25.307955\n",
      "carro 2 se tardo 16.678292\n",
      "carro 4 sale de gasolinera a las 27.307955\n",
      "carro 4 se tardo 10.524295\n",
      "tiempo promedio por vehículo es:  10.148881465813409\n"
     ]
    }
   ],
   "source": [
    "import simpy\n",
    "import random\n",
    "def car(nombre,env,driving_time,bomba):\n",
    "    global totalDia   \n",
    "    yield env.timeout(driving_time)\n",
    "    horaLlegada = env.now \n",
    "    tiempoGas = random.randint(1, 7)\n",
    "    print ('%s llega a las %f necesita %d para hechar gasolina' % (nombre,horaLlegada,tiempoGas)) \n",
    "    with bomba.request() as turno:\n",
    "        yield turno      \n",
    "        yield env.timeout(tiempoGas) \n",
    "        print ('%s sale de gasolinera a las %f' % (nombre, env.now))\n",
    "    tiempoTotal = env.now - horaLlegada\n",
    "    print ('%s se tardo %f' % (nombre, tiempoTotal))\n",
    "    totalDia = totalDia + tiempoTotal\n",
    "env = simpy.Environment() \n",
    "bomba = simpy.Resource(env,capacity = 1)\n",
    "random.seed(10) \n",
    "totalDia = 0\n",
    "for i in range(5):\n",
    "    env.process(car('carro %d'%i,env,random.expovariate(1.0/10),bomba))\n",
    "env.run(until=50)  \n",
    "print (\"tiempo promedio por vehículo es: \", totalDia/5.0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
