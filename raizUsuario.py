def run():    #Una buena práctica al escribir codigo y declarar funciones es usar las especificaciones de codigo al inicio de cada función
    objetivo = int(input("""
                        Introduce un número: """))
    metodo = int(input(""" 
                        1)Busqueda binaria 
                        2)Enumeración exhaustiva 
                        
                        ¿Que metodo deseas utilizar?: """))


    def exhaustiva(objetivo):   #La manera correcta de  hacer éstas especificaciones es al inicio de la función con triple comillas dar 1.-Una descripción clara y concisa de lo que hará la función 2.- Información de los parametros 3.- La invormación que devolverá dicha función
        """
        Calcula el resultado mas aproximado a la raíz cuadrada de un número
        respuesta: Valor con el que comenzará la iteración
        epsilon: Margen de error de la solución
        paso: Variable que dictará el incremento de la iteración
        Imprime el resultado en pantalla
        """
        respuesta = 0.0 
        epsilon = 0.01
        paso = epsilon**2


        while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
            respuesta += paso

        if abs(respuesta**2 - objetivo) >= epsilon:
            print(f"""
                No se encontró la raíz cuadrada del {objetivo}
                """)
        else:
            print(f"""
                La raíz cuadrada del {objetivo} es {respuesta}
                """)

        
    def binaria(objetivo):
        """
        Calcula la raíz cuadrada de un número con una busqueda binaria
        minimo: Punto minimo de la busqueda
        maximo: Punto máximo. El valor "minimo" para el parametro máximo será 1.0
        Epsilon: Margen de error
        Imprime en pantalla el valor de la raíz del número.
        """
        minimo = 0.0
        maximo = max(1.0, objetivo)
        respuesta = (maximo + minimo) / 2 #respuesta de busqueda binaria
        epsilon = 0.01

        while abs(respuesta**2 - objetivo) >= epsilon:
            if respuesta**2 < objetivo:
                minimo = respuesta
            else:
                maximo = respuesta

            respuesta = (maximo + minimo) / 2

        print(f"""
            La raíz cuadrada del {objetivo} es {respuesta}
            """)


    if metodo == 1:
        binaria(objetivo)
    elif metodo == 2:
        exhaustiva(objetivo)
    else:
        print(f"""
            {metodo} no es una opción valida.
            """)
        run()



if __name__ == "__main__":
    run()