"""
Programa 'Quadrado'
Descrição: Este programa lê cinco números e imprime na tela o quadrado de cada um deles.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""
# Definição de entrada de dados:

def entrada_dados():
    dados = []
    i = 0
    while i < 5:
        dados.append(float(input(f'\nDigite a parcela {i + 1}: ')))
        i+=1
    return dados

# Definição da função quadrado dos números:

def dados(x,y,z,k):
    numeros_quadrado = [x ** 2 for x in dados]
    return numeros_quadrado

# Definição da função saída:

def saida_dados(x):
    print(f'\nO quadrados dos números inseridos é, respectivamente, {x}. \n')

# Definição da função principal:

def main():
    dados = entrada_dados()
    numeros = (dados[0], dados[1], dados[2], dados[3], dados[4])
    numeros_quadrado = [x ** 2 for x in numeros]
    saida_dados(numeros_quadrado)

# Execução da função:

main()