"""
Programa Retorno Investimento
Descrição: este programa solicita o valor de um capital, o prazo de investimento, a taxa de juros, calcula e imprima
na tela o valor capitalizado.
Autor: André Azevedo Spader
Data: 15/05/2024
Versão: 1.0.0
"""
# Alocação de memória:

capital_inicial = 0
prazo_investimento = 0
taxa_juros = 0

# Entrada de dados:

capital_inicial = float(input("\nDigite o capital inicial: "))
prazo_investimento = int(input("\nDigite o prazo de investimento em meses: "))
taxa_juros = float(input("\nDigite a taxa de juros anual: "))

# Processamento de dados

prazo_anos = prazo_investimento / 12
taxa_decimal = taxa_juros / 100
delta = 1 + taxa_decimal
delta_a = delta ** prazo_anos
valor_capitalizado = capital_inicial * delta_a
valor_capitalizado_final = round(valor_capitalizado, 2)
formatado = f"{valor_capitalizado_final:.2f}"

# Saída de dados:

print(f'\nO valor capitalizado ao final de {prazo_investimento} meses é de R$ {formatado}. ')