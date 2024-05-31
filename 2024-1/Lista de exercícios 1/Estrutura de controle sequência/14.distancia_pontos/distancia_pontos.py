"""
Programa 'Calculadora de distância entre pontos'
Descrição: este programa calcula a distância entre dois pontos de coordenadas, respectivamente, (x1, x2) e (x1, x2). Tais coordenadas devem ser lidas do teclado, utilizando a fórmula da distância euclideana entre dois pontos.
Autor: André Azevedo Spader
Data: 16/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
x1 = 0
x2 = 0
y1 = 0
y2 = 0

# Entrada de dados
x1 = float(input("\nDigite a coordenada X do Ponto A: "))
x2 = float(input("\nDigite a coordenada Y do Ponto A: "))
y1 = float(input("\nDigite a coordenada X do Ponto B: "))
y2 = float(input("\nDigite a coordenada Y do Ponto B: "))

# Processamento de dados:
import math
distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
formatado = f"{distancia:.2f}"

# Saída de dados:
print(f'\nA distância entre os pontos de coordenada ({x1}, {x2}) e ({y1}, {y2}) é de {formatado} unidades de distância.')