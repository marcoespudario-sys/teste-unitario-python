Atividade da disciplina de Engenharia de Software: Teste unitário.

## 🚀 Funcionalidades

- **Soma (`somar`)**: Realiza a adição de dois números.
- **Subtração (`subtrair`)**: Calcula a diferença entre dois números.
- **Multiplicação (`multiplicar`)**: Retorna o produto de dois números.
- **Divisão (`dividir`)**: Realiza a divisão entre dois números, com tratamento robusto para evitar erros de divisão por zero.
- **Interface CLI**: Um menu interativo no terminal que valida as entradas do usuário, prevenindo quebras por digitação de caracteres inválidos.

## 📁 Estrutura do Projeto

O repositório possui a seguinte estrutura de arquivos:

Saída de código
Arquivo README.md criado com sucesso.

  O prompt utilizado para gerar os testes foi o seguinte:
  "Atue como um professor de Teste de Software.
  Tenho a seguinte função Python:
  
  def potencia(a, b):
      return a ** b
      
  Quero criar testes unitários usando unittest.
  Liste pelo menos 6 cenários de teste para essa função.
  Para cada cenário, informe:
  - nome do cenário;
  - entrada;
  - resultado esperado;
  - tipo do cenário: caso normal, caso de borda ou caso de erro.
  Não gere código ainda. "

E depois pedi para conferir os testes gerados e implementá-los.

Tabela gerada pela IA, para os testes:
| Nome do Cenário | Entrada (a, b) | Resultado Esperado | Tipo do Cenário |
| :--- | :--- | :--- | :--- |
| `test_potencia_caso_padrao` | a = 2, b = 3 | 8 | Caso normal |
| `test_potencia_base_zero_expoente_positivo` | a = 0, b = 5 | 0 | Caso de borda |
| `test_potencia_expoente_zero` | a = 5, b = 0 | 1 | Caso de borda |
| `test_potencia_zero_elevado_a_zero` | a = 0, b = 0 | 1 | Caso de borda crítico |
| `test_potencia_expoente_negativo` | a = 2, b = -2 | 0.25 | Caso de borda |
| `test_potencia_divisao_por_zero_indireta` | a = 0, b = -1 | ZeroDivisionError (Exceção) | Caso de erro |






```text
├── calculadora.py       # Código principal com as funções e interface da calculadora
└── test_calculadora.py  # Arquivo de testes unitários utilizando o framework unittest
