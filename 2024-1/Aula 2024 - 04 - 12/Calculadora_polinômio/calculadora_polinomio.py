"""
Programa Calculadora de Poinômios do Segundo Grau
Descrição: Este programa pede os coeficientes a, b e c de um polinômio de segundo graus e determina as raízes deste polinômio.
Autor: André Azevedo Spader
Data: 17/04/2024
Versão: 1.0.0
"""
# Alocação de memória

a = 0
b = 0
c = 0

# Entrada de dados

a = float(input("\n Digite o termo 'a' do polinômio: \n"))
b = float(input("\n Digite o termo 'b' do polinômio: \n"))
c = float(input("\n Digite o termo 'c' do polinômio: \n"))

# Processamento de dados
quadrado_b = b ** 2
delta = (quadrado_b) - 4 * a * c
raiz_1 = (-b + (delta) ** 0.5) / 2 * a
raiz_2 = (-b - (delta) ** 0.5) / 2 * a

if delta <= 0:
    frase = "\nO polinômio não possui raízes pertencentes aos números reais. \n"
elif a == 0:
    frase = "\nOs dados inseridos não correspondem a um polinômio do segundo grau, pois o termo 'a' não pode ser igual a zero. \n"
else:
    frase = (f"\nAs raízes do polínômio de segundo grau são {raiz_1} e {raiz_2}. \n")

# Saída de dados

print(frase)