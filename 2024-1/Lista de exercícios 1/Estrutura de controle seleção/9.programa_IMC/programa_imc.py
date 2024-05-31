"""
Programa 'IMC'
Descrição: Este programa lê o peso e a altura de uma pessoa, calcula seu índice de massa corporal (IMC), classifique essa pessoa de acordo com a tabela abaixo e escreva na tela a condição da pessoa.
Autor: André Azevedo Spader
Data: 24/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
peso = 0
altura = 0
imc_round = 0

# Entrada de dados:
peso = float(input("\nDigite o peso em quilogramas: \n"))
altura = float(input("\nDigite a altura em metros: \n"))

# Processamento e saída de dados:
imc = peso / (altura * altura)
imc_round = round(imc, 1)

if imc_round <= 18.5:
    print(f'\nO IMC para os dados inseridos é de {imc_round}. A pessoa está excessivamente magra. \n')

elif imc_round > 18.5 and imc_round <= 25:
    print(f'\nO IMC para os dados inseridos é de {imc_round}. A pessoa está com peso normal. \n')

elif imc_round > 25 and imc_round <= 30:
    print(f'\nO IMC para os dados inseridos é de {imc_round}. A pessoa está com sobrepeso. \n')

else:
    print(f'\nO IMC para os dados inseridos é de {imc_round}. A pessoa está obesa. \n')