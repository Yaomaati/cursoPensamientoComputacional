def run():
    #En ocasiones uno no será capaz de encontrar la respuesta exacta a un determinado problema, en éste caso la raíz cuadrada. 
    #Para estos casos se utiliza la aproximación de soluciones, en la cuál emplearemos un margen de error minimo al que llamaremos epsilon.
    #En el siguiente ejemplo intentaremos encontrar la solución mas cercana a la raíz cuadrada de un número determinado
    objetivo = int(input("Elige un número: "))
    epsilon = 0.001 #Este es nuestro margen de error, y cuanto menor sea epsilon, el tiempo requerido para llegar a la respuesta aumentará exponencialmente
    paso = epsilon**2  #Aquí estamos determinando cuando aumentará nuestra iteración en cada paso que de rumbo a la solución
    respuesta = 0.0  #Definimos el punto de partida


    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontró la raíz cuadrada del {objetivo}')
    else:
        print(f'La raíz cuadrada del {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()