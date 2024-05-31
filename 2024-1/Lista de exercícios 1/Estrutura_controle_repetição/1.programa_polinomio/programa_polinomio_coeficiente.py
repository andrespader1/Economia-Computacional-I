"""
Programa 'Polinomio_coeficiente'
Descrição: Este programa calcula o valor de um polinômio de grau 'n' supondo que o usuário informou o grau do polinômio e os coeficientes na ordem da lista ordenada a = (a0, a1, ..., an−1, an) onde 'ai' representa o coeficiente do termo de grau 'i'.
Autor: André Azevedo Spader
Data: 25/05/2024
Versão: 1.0.0
"""

def calcular_polinomio(coeficientes, x):
    grau = len(coeficientes) - 1  # Grau do polinômio
    resultado = 0
    
    for i in range(grau + 1):
        resultado += coeficientes[i] * (x ** i)
    
    return resultado

# Entrada de dados
grau = int(input("Digite o grau do polinômio: "))
coeficientes = []
for i in range(grau + 1):
    coeficiente = float(input(f"Digite o coeficiente a{i}: "))
    coeficientes.append(coeficiente)

x = float(input("Digite o valor de x para calcular o polinômio: "))

# Calcula o valor do polinômio
resultado = calcular_polinomio(coeficientes, x)

# Saída de dados
print(f"O valor do polinômio para x = {x} é: {resultado}")
