"""
Programa 'Raíz Quadrada'
Descrição: Este programa determina a raiz quadrada de um número dado pelo usuário.
Autor: André Azevedo Spader
Data: 24/05/2024
Versão: 1.0.0
"""

# Alocação de memória:
numero = 0
raiz_round = 0

# Entrada de dados:
numero = float(input("\nDigite o número: \n"))

# Processamento e saída de dados:
if numero > 0:
    raiz = numero ** 0.5
    raiz_round = round(raiz, 5)
    print(f'\nA raíz quadrada do numero {numero} é {raiz_round}. \n')

else:
    print(f'\nO número {numero} não é válido. \n')