"""
Programa 'Cubo'
Descrição: Este programa lê 6 números e imprime o cubo e a raiz cúbica de cada um deles.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""

# Definição da função entrada de dados;

def entrada_dados():
    dados = []
    i = 0
    while i < 6:
        dados.append(float(input(f'\nDigite a parcela {i + 1}: ')))
        i += 1
    return dados

# Definição da função processamento de dados:
def dados(x,y,z,k,m,n):
    numeros_cubo = [x ** 3 for x in dados]
    raiz_cubica = [y ** (1/3) for y in dados]
    return numeros_cubo
    return raiz_cubica

# Definição da função saída de dados:
def saida_dados(x, y):
    print(f'\nOs cubos dos números inseridos são, respectivamente, {x}. As raízes cúbicas dos números inseridos são, respectivamente, {y}.')

# Definição da função principal:
def main():
    dados = entrada_dados()
    numeros = (dados[0], dados[1], dados[2], dados[3], dados[4], dados[5])
    numeros_cubo = [x ** 3 for x in numeros]
    raiz_cubica = [y ** (1/3) for y in numeros]
    saida_dados(numeros_cubo, raiz_cubica)

# Execução da função:

main()