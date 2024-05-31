"""
Programa 'Cálculo IR'
Descrição: Dado o número de horas trabalhadas por um empregado de uma empresa que paga R$ 20,00 por hora trabalhada e desconta imposto de renda (IR), este programa determina o salário líquido do empregado.
Autor: André Azevedo Spader
Data: 24/05/2024
Versão: 1.0.0
"""
# Alocação de memória:
horas = 0
salario_bruto = 0
salario_liquido_round = 0

# Entrada de dados:
horas = int(input("\nDigite o número de horas trabalhadas: \n"))

# Processamento de dados:
salario_bruto = horas * 20

if salario_bruto <= 1000:
    salario_liquido_round = f"{salario_bruto:.2f}"
    print(f'\nO salário líquido do funcionário é de R${salario_liquido_round}. \n')

elif salario_bruto > 1000 and salario_bruto <= 2500:
    salario_liquido = salario_bruto * 0.9
    salario_liquido_round = f"{salario_liquido:.2f}"
    print(f'\nO salário líquido do funcionário é de R${salario_liquido_round}. \n')

elif salario_bruto > 2500 and salario_bruto <= 5000:
    salario_liquido = salario_bruto * 0.8
    salario_liquido_round = f"{salario_liquido:.2f}"
    print(f'\nO salário líquido do funcionário é de R${salario_liquido_round}. \n')

else:
    salario_liquido = salario_bruto * 0.65
    salario_liquido_round = f"{salario_liquido:.2f}"
    print(f'\nO salário líquido do funcionário é de R${salario_liquido_round}. \n')