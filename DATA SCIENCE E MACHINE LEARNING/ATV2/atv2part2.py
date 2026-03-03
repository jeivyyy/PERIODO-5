# ATIVIDADE À SEGUIR CONTEMPLA A PRIMERIA PARTE DE EXERCÍCIOS ENVOLVENDO NUMPY

import numpy as np

vendas = np.array([120, 150, 90, 200, 170])

sumArr = np.sum(vendas)
meanArr = np.mean(vendas)
maxArr = np.max(vendas)
minArr = np.min(vendas)
print(f"Soma total: {sumArr}\nMédia: {meanArr}\nMáximo: {maxArr}\nMínimo: {minArr}")

matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
sumLinha = matriz.sum(axis=1)
sumColuna = matriz.sum(axis=0)
timesMatriz = matriz*2
print(f"Matriz: \n{matriz}\nSoma por linha: {sumLinha}\nSoma por coluna: {sumColuna}\n Multiplicação da matriz: \n{timesMatriz}")


