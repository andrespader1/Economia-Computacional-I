"""
Programa 'Calculadora de progressão geométrica'
Descrição: este programa calcula o n-ésimo termo uma progressão geométrica a partir dos dados inseridos pelo usuário, assim como a soma de todos os termos até o n-ésimo termo.
Autor: André Azevedo Spader
Versão: 0.0.1
Data: 25/04/2024
"""
# Alocação de memória

a1 = 0
n = 0
r = 0

# Entrada de dados

a1 = float(input("\nDigite o primeiro termo: \n"))
n = int(input("\nDigite qual termo deseja encontrar: \n"))
r = float(input("\nDigite a razão da PA: \n"))

# Processamento de dados

n_1 = n - 1
an = a1 * r ** n_1

sn = (a1 * ((r ** n) - 1))/ (r - 1)

# Saída de dados

print(f"\nO {n}º termo da progressão geométrica é {an}.")
print(f"A soma dos termos da progressão geométrica no {n}º termo é {sn}. \n")