import pandas as pd 
from matplotlib import pyplot as plt
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression

# +---- REGRESSÕES
#                       {amostras}      {categorias}  {ruído}
x, y = make_regression(n_samples=200, n_features=1, noise=30)
plt.scatter(x,y) # peguei as amostrar e espalhei aleatoriamente

# +---- MODELO LINEAR 
modelo = LinearRegression() # criei o modelo 
modelo.fit(x,y) # ajusto o modelo com base nos dados

ang_coeff = modelo.coef_  # coeficiente angular
lin_coeff = modelo.intercept_ # coeficiente linear

# Y = A + B * X | EQUAÇÃO RESPONSÁVEL POR CRIAR A RETA
y = lin_coeff + (ang_coeff * x)
print(f'Coeficiente angular: {ang_coeff}\nCoeficiente linear: {lin_coeff}')

#       {X}     {equação linear}
plt.plot(x, lin_coeff + ang_coeff * x, color='red')

plt.scatter(2.5, lin_coeff + ang_coeff * 2.5, color='green') # testando em um ponto especifíco

plt.show() # MOSTRAR GRÁFICO COM A RETA