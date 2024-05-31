"""
Programa 'Ordem Crescente'
Definição: este programa lê do teclado 3 valores reais e os imprime na tela em ordem crescente.
Autor: André Azevedo Spader
Data: 16/05/2024
Versão: 1.0.0
"""

# Definição da função de entrada:

def entrada_dados():
    dados = []
    i = 0
    while i < 3:
        dados.append(float(input(f'\nDigite a parcela {i + 1}: ')))
        i+=1
    return dados

# Definição da função ordenamento:

def dados(x,y,z):
    numeros_ordenados = sorted(dados)
    return numeros_ordenados

# Definição da função saída:

def saída_dados(x):
    print(f'\nA ordem dos números inseridos é {x}')

# Definição da função principal:

def main():
    dados = entrada_dados()
    numeros = (dados[0], dados[1], dados[2])
    numeros_ordenados = sorted(numeros)
    saída_dados(numeros_ordenados)

# Execução da função

main()