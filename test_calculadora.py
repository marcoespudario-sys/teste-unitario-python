import unittest
# Importa as funções da calculadora
from calculadora import somar, subtrair, multiplicar, dividir

class TestCalculadora(unittest.TestCase):

    def test_somar(self):
        """Testa a função de soma com números positivos, negativos e zero."""
        self.assertEqual(somar(5, 3), 8)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(-2, -3), -5)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa a função de subtração."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(0, 5), -5)
        self.assertEqual(subtrair(-3, -3), 0)

    def test_multiplicar(self):
        """Testa a função de multiplicação."""
        self.assertEqual(multiplicar(4, 3), 12)
        self.assertEqual(multiplicar(-2, 3), -6)
        self.assertEqual(multiplicar(5, 0), 0)

    def test_dividir(self):
        """Testa a função de divisão, incluindo o caso de divisão por zero."""
        self.assertEqual(dividir(10, 2), 5.0)
        self.assertEqual(dividir(5, 2), 2.5)
        self.assertEqual(dividir(-6, 2), -3.0)
        
        # Testa a mensagem de erro esperada para a divisão por zero
        erro_divisao_zero = "Erro: Divisão por zero não é permitida!"
        self.assertEqual(dividir(5, 0), erro_divisao_zero)

if __name__ == "__main__":
    unittest.main()
