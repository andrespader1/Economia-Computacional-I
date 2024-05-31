"""
Programa 'Calculadora de salário de professor da Universidade XYZ'
Descrição: Este programa calcula o salário de um professor horista na Univeridade XYZ. O programa pergunta o número de horas trabalhadas, calcula e imprime na tela o valor do salário bruto, do salário líquido e do total de descontos, sabendo que o desconto do imposto é de 30% e que o valor da hora-aula é de R$ 40,00.
Autor: André Azevedo Spader
Data: 17/04/2024
Versão: 1.0.0
"""
# Alocação de memória

horas_trabalhadas = 0
valor_hora = 40
casas_decimais = 2

# Entrada de dados

horas_trabalhadas = float(input("\nDigite a quantidade de horas trabalhadas: \n"))

# Processamento de dados

salario_bruto = horas_trabalhadas * 40
descontos = salario_bruto * 0.30
salario_liquido = salario_bruto - descontos

# Saída de dados

print(f"\nO salário bruto do professor corresponde a R$ {salario_bruto:.{casas_decimais}f}.")
print(f"\nOs descontos correspondem a soma de R$ {descontos:.{casas_decimais}f}.")
print(f"\nO salário liquido do professor corresponde a R$ {salario_liquido:.{casas_decimais}f}.")