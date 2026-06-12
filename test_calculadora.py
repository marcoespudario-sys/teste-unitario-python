
# test_calculadora.py

import unittest

from calculadora import dividir, multiplicar, somar, subtrair, potencia


class TestCalculadora(unittest.TestCase):
    """Classe de testes para as funções do arquivo calculadora.py."""

    def test_somar(self):
        """Testa se a função somar está funcionando corretamente."""
        self.assertEqual(somar(2, 3), 5)
        self.assertEqual(somar(-1, 1), 0)
        self.assertEqual(somar(0, 0), 0)

    def test_subtrair(self):
        """Testa se a função subtrair está funcionando corretamente."""
        self.assertEqual(subtrair(10, 5), 5)
        self.assertEqual(subtrair(5, 10), -5)
        self.assertEqual(subtrair(0, 0), 0)

    def test_multiplicar(self):
        """Testa se a função multiplicar está funcionando corretamente."""
        self.assertEqual(multiplicar(3, 4), 12)
        self.assertEqual(multiplicar(5, 0), 0)
        self.assertEqual(multiplicar(-2, 3), -6)

    def test_dividir(self):
        """Testa se a função dividir está funcionando corretamente."""
        self.assertEqual(dividir(10, 2), 5)
        self.assertEqual(dividir(9, 3), 3)
        self.assertEqual(dividir(5, 2), 2.5)

    def test_dividir_por_zero(self):
        """Testa se a divisão por zero gera erro."""
        with self.assertRaises(ZeroDivisionError):
            dividir(10, 0)

   # def test_potencia(self):
       # """Testa a função de potência com diferentes bases e expoentes."""
       # self.assertEqual(potencia(2, 3), 8)
      #  self.assertEqual(potencia(5, 0), 1)
       # self.assertEqual(potencia(10, 2), 100)

    def test_calcular_media(self):
        """Testa a função de calcular média com diferentes cenários de listas."""
        # 1. Lista com números inteiros
        self.assertEqual(calcular_media([10, 8, 6]), 8)
        
        # 2. Lista com números decimais
        self.assertEqual(calcular_media([1.5, 2.5, 3.5, 4.5]), 3.0)
        
        # 3. Lista com apenas um número
        self.assertEqual(calcular_media([7]), 7)
        
        # 4. Lista vazia (deve gerar um erro ValueError)
        with self.assertRaises(ValueError):
            calcular_media([])

##Teste gerado pela IA: função escolhida foi potencia

def test_potencia_caso_padrao(self):
        """Cenário 1: Testa a lógica básica da exponenciação com inteiros positivos."""
        self.assertEqual(potencia(2, 3), 8)

    def test_potencia_base_zero_expoente_positivo(self):
        """Cenário 2: Testa o comportamento da base sendo zero com expoente positivo."""
        self.assertEqual(potencia(0, 5), 0)

    def test_potencia_expoente_zero(self):
        """Cenário 3: Testa a propriedade matemática de número diferente de zero elevado a zero."""
        self.assertEqual(potencia(5, 0), 1)

    def test_potencia_zero_elevado_a_zero(self):
        """Cenário 4: Testa o caso de borda crítico de zero elevado a zero (convenção do Python)."""
        self.assertEqual(potencia(0, 0), 1)

    def test_potencia_expoente_negativo(self):
        """Cenário 5: Testa expoente negativo, forçando o retorno de um tipo float."""
        self.assertEqual(potencia(2, -2), 0.25)

    def test_potencia_divisao_por_zero_indireta(self):
        """Cenário 6: Testa se base zero com expoente negativo lança a exceção ZeroDivisionError."""
        with self.assertRaises(ZeroDivisionError):
            potencia(0, -1)

if __name__ == "__main__":
    unittest.main()
