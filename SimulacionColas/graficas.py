
import matplotlib.pyplot as plot

def plotear(intervalo,datos1,datos2):
    intervalo1 = getIntervalos(intervalo,len(datos1))
    intervalo2 = getIntervalos(intervalo,len(datos2))
    plot.figure()

    plot.subplot(2,2,1)
    plot.plot(intervalo1,datos1,linestyle='--', marker='o', color='b')

    plot.subplot(2, 2, 2)
    plot.plot(intervalo2, datos2, linestyle='--', marker='o', color='r')

    plot.show()


def getIntervalos(intervalo,cantidad_datos):

    datos = list()
    intervalos = 0

    for control in range(cantidad_datos):
        intervalos = intervalos + intervalo
        datos.append(round(intervalos,2))

    return datos