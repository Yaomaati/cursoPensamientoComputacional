#En éste tipo de pruebas nos aseguramos que un pedazo individual de código este funcionando.
#Al establecer cuál es el resultado que estamos esperando para que sea comparado con el que arroja finalmente dicho codigo.
#En otras palabras es mas comunmente utilizado para revisión de codigo que estamos por desarrollar.

import unittest

def suma(num1, num2):
    return num1 + num2

class CajaNegraTest(unittest.TestCase):

    def test_suma_positivos(self):
        num1 = 3
        num2 = 7

        resultado = suma(num1, num2)

        self.assertEqual(resultado, 10)



if __name__ == "__main__":
    unittest.main()