"""
Programa 'Função Demanda'
Descrição: este programa utiliza dados sobre a renda do consumidor e o preço de um bem, e calcula a quantidade de demandada deste bem.
Autor: André Azevedo Spader
Data: 16/05/2024
Versão: 1.0.0
"""

# Alocação de memória:
renda = 0
preço = 0

# Entrada de dados:
renda = float(input("\nDigite o valor da renda do consumidor: "))
preço = float(input("\nDigite o valor do preço do bem: "))

# Processamento de dados:
qnt_demandada = renda / preço
qnt_final = round(qnt_demandada)

# Saída de dados:
print(f'\nA quantidade demandada do bem, para os dados inseridos, é de {qnt_final} unidades.')