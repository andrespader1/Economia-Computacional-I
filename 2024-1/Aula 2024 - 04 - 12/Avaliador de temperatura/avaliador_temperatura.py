"""
Programa Avaliador de Temperatura:
Descrição: este programa perguta ao usuário a temperatura do ambiente
Autor: André Azevedo Spader
Data: 16/04/2024
Versão: 1.0.0
"""

# Alocação de memória

temperatura = 0

# Entrada de dados

temperatura = float(input("\nInforme a temperatura do ambiente: \n"))

# Processamento de dados

if temperatura <= 18:
    frase = "\nEstá frio. \n"
elif temperatura > 18 and temperatura <= 28:
    frase = "\nEstá agradável. \n"
else:
    frase = "\nEstá quente. \n"
    
# Saída de dados

print(frase)