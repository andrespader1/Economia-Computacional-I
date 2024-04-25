"""
Programa busca_sequencial.py
Descrição: Este programa busca um valor em uma base de dados.
Autor: André Azevedo Spader
Versão: 0.0.3
Correções: 
1. Informações mais precisas de que o valor encontrado é um CPF
2. Não se informa mais a posição onde o CPF foi encontrado no banco de dados, mas essa versão é mais rápida e legível que a versão anterior.
data: 19/04/2024
"""

## Alocação de memória

lista = []
achou = False
posicao = 0
cpf = 0

# Leitura da base de dados de cpf

base = [1,5,2,87,31]
lista = base

# Leitura de dados

cpf = int(input("Digite o CPF a procurar: "))

# Processamento de dados

for elem in lista:
    if elem == cpf:
        achou = True
        break

# Saída de dados:


if achou:
    print(f"\nO CPF {cpf} foi achado")
else:
    print(f"\nO CPF {cpf} não foi achado.")
