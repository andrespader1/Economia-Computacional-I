"""
Programa 'Idade'
Descrição: Este programa lê o nome e a idade de uma pessoa. Se a pessoa tiver menos de 18 anos, imprime"[nome] não pode assistir a este filme.”, onde no lugar de [nome] deve sair o nome lido do teclado.
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""
# Alocação de memória:

nome = ""
idade = 0

# Entrada de dados:

nome = input("\nDigite o nome da pessoa: \n")
idade = int(input("\nDigite a idade: \n"))

# Processamento e saída de dados:

if idade < 18:
    print(f'\n{nome} não pode assistir a esse filme. \n')

else:
    print(f'\n{nome} pode assistir a esse filme. \n')