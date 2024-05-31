"""
Programa 'Múltiplo"
Descrição: Estre programa lê um número e imprime na tela o seu dobro se ele for menor do que 10. Se o número for de 10 até 20, imprime a sua metade. Em qualquer outro caso, imprime na tela que o número não é válido.
Autor: André Azevedo Spader
Data: 23/05/2024
Versão: 1.0.0
"""
# Alocação de memória:

número = 0

# Entrada de dados:

numero = float(input("\nDigite o número: "))

# Processamento e saída de dados:

if numero < 10:
    print(f'{numero * 2}')
elif numero >= 10 and numero <= 20:
    print(f'{numero / 2}')
else:
    print("\nEste número não é válido.")