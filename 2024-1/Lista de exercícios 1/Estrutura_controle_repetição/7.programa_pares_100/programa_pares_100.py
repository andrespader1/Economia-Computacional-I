"""
Programa 'Pares 100'
Descrição: Este programa imprime na tela todos os números pares de 0 a 100.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""

# Processamento e saída de dados:
num = 0
for num in range(101):
    if num % 2 == 0:
        print(num, end= ' ')