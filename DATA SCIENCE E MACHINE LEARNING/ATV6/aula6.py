import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

opt = int(input("""
            +=========================================+ 
            |    'Selecione uma das amostrar abaixo:  |  
            |      1 - Teste: IRIS                    |
            |      2 - Teste: WINE                    |
            |      R:                                 |
            +=========================================+
                """))
match opt:
    case 1:
        iris_str = r""" 
         __     ______     __     ______    
        /\ \   /\  == \   /\ \   /\  ___\   
        \ \ \  \ \  __<   \ \ \  \ \___  \  
         \ \_\  \ \_\ \_\  \ \_\  \/\_____\ 
          \/_/   \/_/ /_/   \/_/   \/_____/
                    """
        print(f"\n {"=" * 100} \nIniciando teste: {iris_str}\n")
        
        # +-------------------------------------+
        #               Importando dados!
        # +-------------------------------------+

        iris = load_iris()
        x_iris = iris.data
        y_iris = iris.target
        
        print(f'\nTotal de amostras: {x_iris.shape[0]}\n')
        print("\n" + "=" * 100)

        # +-------------------------------------+
        #             Treinar e testar
        # +-------------------------------------+

        x_train_iris, x_test_iris, y_train_iris, y_test_iris = train_test_split(
            x_iris, y_iris, test_size=0.30, random_state=43
        )

        # +-------------------------------------+
        #       Normalização de dados
        # +-------------------------------------+

        scaler_iris = StandardScaler()
        scaler_iris.fit(x_train_iris)
           
        x_train_iris = scaler_iris.transform(x_train_iris)
        x_test_iris= scaler_iris.transform(x_test_iris)

        ##+----------- Modelo -----------
        knn_iris = KNeighborsClassifier(n_neighbors=3)
        knn_iris.fit(x_train_iris, y_train_iris)

        #+----------- Previsões -----------
        previsoes_iris = knn_iris.predict(x_test_iris)

        #+----------- Avaliação -----------
        accuracy_iris = accuracy_score(y_test_iris, previsoes_iris)
        print(f'Acurácia do Dataset IRIS: {accuracy_iris * 100: .2f}% das flores classificadas corretamente')

        plt.figure(figsize=(6, 4))
        sns.heatmap(confusion_matrix(y_test_iris, previsoes_iris),annot=True, cmap="Greens", fmt="d",
                    xticklabels=iris.target_names, yticklabels=iris.target_names)

        plt.title('Acertos e erros - IRIS')
        plt.xlabel('Previsões do KNN')
        plt.ylabel('O que era na realidade')
        plt.show()
        
    case 2:
        wine_str = r"""
         __     __     __     __   __     ______    
        /\ \  _ \ \   /\ \   /\ "-.\ \   /\  ___\   
        \ \ \/ ".\ \  \ \ \  \ \ \-.  \  \ \  __\   
         \ \__/".~\_\  \ \_\  \ \_\\"\_\  \ \_____\ 
          \/_/   \/_/   \/_/   \/_/ \/_/   \/_____/                                 
                    """
        print(f"\n {"=" * 100} \nIniciando teste: {wine_str}\n")
        
        # +-------------------------------------+
        #               Importando dados!
        # +-------------------------------------+

        wine = load_wine()
        x_wine = wine.data
        y_wine = wine.target
        
        print(f'\nTotal de amostras: {x_wine.shape}\n')
        print("\n" + "=" * 100)

        # +-------------------------------------+
        #             Treinar e testar
        # +-------------------------------------+

        x_train_wine, x_test_wine, y_train_wine, y_test_wine = train_test_split(
            x_wine, y_wine, test_size=0.20, random_state=42
        )

        # +-------------------------------------+
        #       Normalização de dados
        # +-------------------------------------+

        scaler_wine = StandardScaler()
        scaler_wine.fit(x_train_wine)
           
        x_train_wine = scaler_wine.transform(x_train_wine)
        x_test_wine= scaler_wine.transform(x_test_wine)

        # +----------- Modelo -----------
        knn_wine = KNeighborsClassifier(n_neighbors=5)
        knn_wine.fit(x_train_wine, y_train_wine)

        # +----------- Previsões -----------
        previsoes_wine = knn_wine.predict(x_test_wine)

        # +----------- Avaliação -----------
        accuracy_wine = accuracy_score(y_test_wine, previsoes_wine)
        print(f'Acurácia do Dataset Wine: {accuracy_wine * 100: .2f}% dos vinhos classificados corretamente')

        # plt.figure(figsize=(6, 4))
        sns.heatmap(confusion_matrix(y_test_wine, previsoes_wine),annot=True, cmap="Purples", fmt="d",
                    xticklabels=wine.target_names, yticklabels=wine.target_names)

        plt.title('Acertos e erros - Wine')
        plt.xlabel('Previsões do KNN')
        plt.ylabel('O que era na realidade')
        plt.show()
        
    case _:
        print('>>Opção Invalida<<')
