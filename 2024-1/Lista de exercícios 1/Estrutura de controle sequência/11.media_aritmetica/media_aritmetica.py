"""
Programa Calculadora Média Artimética
Descrição: este programa calcula a média aritmética de quatro números fornecidos pelo usuário.
Autor: André Azevedo Spader
Data: 15/05/2024
Versão: 1.0.0
"""

# Definição da função de entrada:

def entrada_dados():
    dados = []
    i = 0
    while i < 4:
        dados.append(float(input(f'\nDigite a parcela {i + 1}: ')))
        i += 1
    return dados

# Definição da função divisão:

def soma(x,y,z,k):
    resultado_soma = x + y + z + k
    return resultado_soma

# Definição da função saída:

def saída_dados(x):
    print(f'\nO resultado é {x}.')

# Definição da função principal:

def main():
    dados = entrada_dados()
    resultado_soma = soma(dados[0], dados[1], dados[2], dados[3])
    divisão = resultado_soma / 4
    saída_dados(divisão)

# Execução da função

main()