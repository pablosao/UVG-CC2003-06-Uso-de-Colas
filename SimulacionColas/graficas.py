
import matplotlib.pyplot as plot

def plotear(intervalo,datos):
    intervalo = getIntervalos(intervalo,len(datos))
    print(intervalo)
    plot.plot(intervalo,datos,linestyle='--', marker='o', color='b')
    plot.show()


def getIntervalos(intervalo,cantidad_datos):

    datos = list()
    intervalos = 0

    for control in range(cantidad_datos):
        intervalos = intervalos + intervalo
        datos.append(round(intervalos,2))

    return datos