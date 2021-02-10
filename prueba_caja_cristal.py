#En éste tipo de pruebas se utilizan para identificar bugs/errores en código de sofware que ya esta siendo utilizado
#Es decir código ya existente

import unittest

abuelo = 20
nieto = 12

def mayoria_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    
    def test_mayor_de_edad(self):
        edad = abuelo

        resultado = mayoria_de_edad(edad)

        self.assertEqual(resultado, True)

    def test_menor_de_edad(self):
        edad = nieto

        resultado = mayoria_de_edad(edad)

        self.assertEqual(resultado, False)

if __name__ == '__main__':
    unittest.main()