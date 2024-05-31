"""
Programa 'Potência'
Descrição: Este programa lê dois números 'a' e 'b' e calcule a potência de 'a' em 'b' sem utilizar uma função nativa do Python.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""

# Alocação de memória:
a = 0
b = 0

# Entrada de dados:
a = float(input("\nDigite o número base: \n"))
b = float(input("\nDigite o expoente: \n"))

# Processamento de dados:
resultado = a ** b

# Saída de dados:
print(f'\nO resultado da potência de base {a} e expoente {b} é {resultado}. \n')