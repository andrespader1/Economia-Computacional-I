"""
Programa 'Capital'
Descrição: Este programa lê um texto e informa se ele é o nome da capital de um estado da região sul do Brasil.
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""

# Alocação de dados:
nomes_a_verificar = ""

# Entrada de dados:
nome_a_verificar = input("\nDigite o nome da cidade: \n")

# Processamento de dados:
if nome_a_verificar in ["Porto Alegre", "porto alegre", "portoalegre"]:
    print(f'\nPorto Alegre é capital do Rio Grande do Sul. \n')
elif nome_a_verificar in ["Florianópolis", "florianopolis", "Florianopolis", "florianopolis"]:
    print(f'\nFlorianópolis é capital de Santa Catarina. \n')
elif nome_a_verificar in ["Curitiba", "curitiba"]:
    print(f'\nCuritiba é capital do Paraná. \n')
else:
    print(f'\n{nome_a_verificar} não é capital de nenhum estado do Sul. \n')