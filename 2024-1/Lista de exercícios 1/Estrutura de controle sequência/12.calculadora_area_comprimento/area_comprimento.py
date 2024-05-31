"""
Programa 'Calculadora área e comprimento do círculo'
Descrição: este programa calcula a área e o comprimento de um círculo cujo raio é dado pelo usuário.
Autor: André Azevedo Spader
Data: 15/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
raio = 0

# Entrada de dados
raio = float(input("\nDigite o raio do círculo em centímetros: "))

# Processamento de dados:
import math
area = math.pi * raio ** 2
comprimento = 2 * math.pi * raio
area_r = f"{area:.5f}"
comprimento_r = f"{comprimento:.5f}"

# Saída de dados:
print(f'\nO círculo de raio {raio} centímentros possui área de {area_r} centímetros e comprimento de {comprimento_r} centímetros.')