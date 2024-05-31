"""
Programa 'Notas'
Descrição: Este programa solicita as notas de um aluno nas avaliações previstas no plano de ensino desta disciplina, calcula a sua média e informe se o aluno está aprovado ou reprovado com base nas notas obtidas, incluindo a recuperação.
Autor: André Azevedo Spader
Data: 24/05/2024
Versão: 1.0.0
"""

# Alocação de memória
teste_1 = 0
teste_2 = 0
prova_final = 0
recuperacao = 0
nota_round = 0
media_final_round = 0

# Entrada de dados inicial
teste_1 = float(input("\nDigite a nota do Teste 1: \n"))
teste_2 = float(input("\nDigite a nota do Teste 2: \n"))
prova_final = float(input("\nDigite a nota da Prova Final: \n"))

# 1º Processamento de dados
teste_1_def = teste_1 * 0.15
teste_2_def = teste_2 * 0.15
prova_final_def = prova_final * 0.7
nota_final = teste_1_def + teste_2_def + prova_final_def
nota_round = round(nota_final, 1)

# 2º Processamento de dados
if nota_round >= 6:
    print(f'\nO aluno está APROVADO com média final {nota_round}. \n')

elif nota_round < 6:
    recuperacao = float(input("\nDigite a nota de recuperação: \n"))
    media_final = (3 * recuperacao + 2 * nota_round) / 5
    media_final_round = round(media_final, 1)
    
    if media_final_round >= 6:
            print(f'\nO aluno está APROVADO com média final {media_final_round}. \n')
    else:
            print(f'\nO aluno está REPROVADO com média final {media_final_round}. \n')
else:
    print("\nOs valores computados são inválidos. \n")