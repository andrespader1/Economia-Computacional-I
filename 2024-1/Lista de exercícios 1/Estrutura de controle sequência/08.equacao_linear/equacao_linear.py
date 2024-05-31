"""
Programa 'Calculadora equação linear'
Descrição: este programa resolve uma equação linear a.x = b
Autor: André Azevedo Spader
Data: 15/05/2024
Versão: 1.0.0
"""
# Alocação de memória

coeficiente_a = 0
coeficiente_b = 0

# Entrada de dados

coeficiente_a = float(input("\nDigite o coeficiente 'a': "))
coeficiente_b = float(input("\nDigite o coeficiente 'b': "))

# Processamento de dados

resultado = coeficiente_b / coeficiente_a

# Saída de dados

print(f"\nO resultado da equação {coeficiente_a}x = {coeficiente_b} é x = {resultado}")