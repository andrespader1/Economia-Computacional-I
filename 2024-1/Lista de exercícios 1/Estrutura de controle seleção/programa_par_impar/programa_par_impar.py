"""
Programa 'Par / Impar'
Descrição: Este programa lê um número e imprima na tela a mensagem "O número é par.” se o número lido for par e "O número é impar” se o número lido for ímpar. Em caso de número não inteiros ou negativos, imprime na tela "Este número não é válido.”
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""

# Alocação de memória:

numero = 0

# Entrada de dados:

numero = float(input("\nDigite o número: \n"))

# Processamento e saída de dados:

if numero.is_integer():
    numero = int(numero)

    if numero % 2 == 0:
        print("\nO número é par. \n")
    else:
        print("\nO número é impar. \n")

else:
    print("\nO número não é válido. \n")