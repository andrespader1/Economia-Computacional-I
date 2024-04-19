"""
Programa soma
Descrição: Este programa lê dois números inteiros digitados pelo usuário e põe na tela a soma deles.
Autor: André Azevedo Spader
Data: 12/04/2024
Versão: 0.0.2
"""

# Alocação de mmemória

numero: int = 0
i = 0
soma: int = 0

# Entrada e processamento de dados

while i < 2:
    numero = int(input(f"Digite a parcela {i + 1}: "))
    soma = soma + numero
    i += 1

# Saida de dados

print(f"A soma dos números é igual a {soma}")