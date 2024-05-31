"""
Programa 'Pares'
Descrição: Este programa imprime na tela todos os números pares entre 0 e 20.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""

# Processamento e saída de dados:
num = 0
for num in range(21):
    if num % 2 == 0:
        print(num, end= ' ')