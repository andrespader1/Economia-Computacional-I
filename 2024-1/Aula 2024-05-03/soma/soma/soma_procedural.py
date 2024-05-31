"""

"""
# Definição de funções

# Definição da função de entrada
def entrada_dados():
    dados = []
    i = 0
    while i < 2:
         dados.append(int(input(f'\nDigite a parcela {i + 1}: ')))
         i+=1
    return dados

# Definição da função soma
def soma(numero_1, numero_2):
    resultado = numero_1 + numero_2
    return resultado

# Definição da função saída
def saida_dados(x):
    print(f'\nA soma é igual a {x}.')

# Função principal
def main():
    dados = entrada_dados()
    soma(dados[0], dados [1])
    resultado = soma(dados[0], dados[1])
    saida_dados(resultado)

# Excecução da função principal.
main()