"""
Programa Conversor de distâncias
Descrição: Este é um porgrama que lê um valor em metros e o converte para um valor em milímetros
Autor: André Azevedo Spader
Data: 12/04/2024
Versão: 0.0.1
"""

# Alocação de memória

numero = 0
constante = 1000
multiplicação = 0

# Entrada de dados

numero = float(input("Digite o valor em metros: "))

# Processamento de dados

multiplicação = numero * constante

# Saída de dados

print(f"\nO valor {numero} metros corresponde a {multiplicação} milímetros.\n")