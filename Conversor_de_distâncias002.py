"""
Programa Conversor de distâncias
Descrição: Este é um porgrama que lê um valor em metros e o converte para um valor em milímetros
Autor: André Azevedo Spader
Data: 12/04/2024
Versão: 0.0.2
"""

# Alocação de memória

metros: float = 0
milimetros: float = 0

# Entrada de dados

metros = float(input("Digite a distância em metros: "))

# Processamento de dados

milimetros = 1000*metros

# Saída de dados

print(f"\nA distância em milímetros é igual a {milimetros}.\n")