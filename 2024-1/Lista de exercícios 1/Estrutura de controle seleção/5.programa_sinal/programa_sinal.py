"""
Programa 'Sinal'
Descrição: Este programa lê um número e imprime na tela se ele é negativo, nulo ou positivo.
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""

# Alocação de dados:
numero = 0

# Entrada de dados:
numero = float(input("\nDigite o número: \n"))

# Processamemto de dados:
if numero > 0:
    print(f'\nO número {numero} é positivo. \n')
elif numero < 0:
    print(f'\nO número {numero} é negativo. \n')
else:
    print(f'\nO número {numero} é nulo. \n')