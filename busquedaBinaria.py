def run():

    objetivo = int(input('Introduce un número: '))
    epsilon = 0.0001
    minimo = 0.0
    maximo = max(1.0, objetivo)
    respuesta = (maximo + minimo) / 2


    while abs(respuesta**2 - objetivo) >= epsilon:
        if respuesta**2 < objetivo:
            minimo = respuesta
        else:
            maximo = respuesta

        respuesta = (maximo + minimo) / 2

    print(f'La raíz cuadrada del {objetivo} es {respuesta}')


if __name__ == '__main__':
    run()