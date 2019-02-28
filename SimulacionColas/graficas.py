'''
Graficación de dos listas distintas, en un mismo intervalo.
Desplegadas de forma independiente en una misma ventana
@author: Pablo Sao
@date: 26-02-2019
'''

#Importando libreria para graficar
import matplotlib.pyplot as plot

def plotear(intervalo,datos1,titulo_dato1,datos2,titulo_dato2):
    '''
    Graficación de dos listas de datos distintas que comparten un intervalo

    :param intervalo: Intervalo de la gráfica
    :param datos1: lista con los datos de la primera gráfica
    :param titulo_dato1: titulo de la primera gráfica
    :param datos2: lista con los datos de la segunda grafica
    :param titulo_dato1: titulo de la segunda gráfica
    :return:
    '''

    #Obtenemos los intervalos de cada uno de los valores de la lista
    intervalo1 = getIntervalos(intervalo,len(datos1))
    intervalo2 = getIntervalos(intervalo,len(datos2))


    plot.figure()

    #Seteamos los datos de la primera grafica

    plot.subplot(2,2,1)
    plot.title("Gráfica de {0}".format(titulo_dato1))
    plot.plot(intervalo1,datos1,linestyle='--', marker='o', color='b')

    # Seteamos los datos de la segunda grafica
    plot.subplot(2, 2, 2)
    plot.title("Gráfica de {0}".format(titulo_dato2))
    plot.plot(intervalo2, datos2, linestyle='--', marker='o', color='r')

    #mostramos la grafica
    plot.show()


def getIntervalos(intervalo,cantidad_datos):
    '''
    Obtención de la lista de intervalos para una lista

    :param intervalo: factor de los intervalos para los datos
    :param cantidad_datos: numero de registros del intervalo
    :return: lista de intervalos de cada uno de los valores de la lista
    '''

    #Variables temporales para el manejo de información
    datos = list()
    intervalos = 0

    for control in range(cantidad_datos):
        #al valor del intervalos, se sumamos el factor de intervalo para cada cantidad de la lista
        intervalos = intervalos + intervalo
        #Agregamos el valor a una lista
        datos.append(round(intervalos,2))

    return datos