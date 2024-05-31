"""
Programa 'Termo PA'
Descrição: Este programa imprime na tela os 10 primeiros termos de uma progressão aritmética cuja razão é dada pelo usuário.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
a1 = 0
r = 0
n_1 = 0

# Entrada de dados:
a1 = float(input("\nDigite o primeiro termo: "))
r = float(input("\nDigite a razão: "))

# Processamento e saída de dados:

while n_1 < 10:
    an = n_1 * r + a1
    print(an)
    n_1+=1