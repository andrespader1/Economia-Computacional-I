"""
Programa 'Múltiplo de 3'
Descrição: Este programa lê um número, determina se ele é múltiplo de 3 e imprime na tela a mensagem "Este número é múltiplo de 3" ou "Este número não é múltiplo de 3” a depender do caso.
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
numero = 0

# Entrada de dados:
numero = float(input("\nDigite o número: "))

# Processamento e saída de dados:
if numero.is_integer():
    numero = int(numero)

    if numero % 3 == 0:
        print("\nEste número é múltiplo de 3. \n")
    else:
        print("\nEste número não é múltiplo de 3. \n")

else:
    print("\nEste número não é um inteiro válido múltiplo de 3. \n")