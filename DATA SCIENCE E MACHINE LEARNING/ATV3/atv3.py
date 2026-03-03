import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns 
sns.set_style('dark')

ping = sns.load_dataset('penguins') 

ping.columns = ['Espécies', 'ILha', 'Comprimento do bico', 'Largura do bico','Comprimento da asa', 'Massa corporal (g)', 'Sexo']
# sns.displot(ping['Comprimento do Bico'], bins = 30, kde = True)
# sns.histplot(ping['Comprimento do Bico'], bins = 30, kde = True)

# plt.title("Histplot")
# plt.show()

sns.jointplot(data= ping, x= "Comprimento do bico", y= "Largura do bico", hue= "Espécies")
plt.show()
