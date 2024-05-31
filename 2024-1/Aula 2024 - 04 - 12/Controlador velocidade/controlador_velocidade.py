"""
Programa Controlador de Velocidade
Descrição: Este programa que pergunta a velocidade do carro dos usuários. Caso ultrapasse 80 km/h, exibe uma mensagem dizendo que o usuário foi multado. Nesse caso, exibe o valor da multa, cobrando R$ 5,00 por km acima de 80km/h.
Autor: André Azevedo Spader
Data: 16/04/2024
Versão: 1.0.0
"""

# Alocação de memória

velocidade = 0
multa = 5

# Entrada de dados

velocidade  = float(input("\nDigite a velocidade do veículo: \n"))

# Processamento de dados

if velocidade <= 80:
    velocidade_arredondada = round(velocidade)
    frase = f"\nO condutor está dentro do limite de velocidade permitido na via\n."
else:
    velocidade_arredondada = round(velocidade)
    numero = (velocidade_arredondada - 80) * 5
    frase = f"\nO condutor está multado! O valor da multa é de R$ {numero},00. \n"
    
# Saída de dados

print(frase)