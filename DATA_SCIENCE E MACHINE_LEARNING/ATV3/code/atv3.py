import pandas as pd

from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder

# === QUESTÃO 4 - Escreva um código em Pandas para: identificar valores nulos substituir pela mediana da coluna ===

dados1 = [
    ["Daniela"  ,37,"M","Porto Alegre","Médico",11448.67],
    ["Eduardo"  ,46,"F","Curitiba","Analista",None],
    ["Helena"   ,31,"F","São Paulo","Designer",1612.09],
    ["Juliana"  ,45,"M","Curitiba","Vendedor",2003.0],
    ["Carlos"   ,None,"F","Porto Alegre","Professor",10911.05],
    ["Helena"   ,45,"M","Rio de Janeiro","Engenheiro",8824.75],
    ["Ana"      ,62 ,"M","São Paulo","Analista",5639.72],
    ["Daniela"  ,57,"M","Belo Horizonte","Engenheiro",None],
    ["Gabriel"  ,34,"F","Porto Alegre","Designer",7009.27],
    ["Bruno"    ,20,"F","Recife","Professor",6451.19],
    ["Juliana"  ,20,"M","Rio de Janeiro","Vendedor",9047.16],
    ["Bruno"    ,44,"F","Curitiba","Designer",12586.36],
    ["Igor"     ,28,"F","Salvador","Designer",14734.57],
    ["Bruno"    ,20,"F","Porto Alegre","Programador",9289.8],
    ["Helena"   ,None,"F","São Paulo","Programador",None],
    ["Ana"      ,22,"F","Salvador","Analista",9390.28],
    ["Juliana"  ,26,"M","Belo Horizonte","Engenheiro",1630.53],
    ["Bruno"    ,53,"M","Rio de Janeiro","Professor",11837.9],
    ["Igor"     ,27,"M","Porto Alegre","Médico",10362.44],
    ["Juliana"  ,30,"F","Rio de Janeiro","Médico",7777.68],
    ["Igor"     ,30,"F","Rio de Janeiro","Vendedor",None],
    ["Fernanda" ,50,"F","Curitiba","Médico",None],
    ["Daniela"  ,33,"F","Salvador","Professor",1693.07],
    ["Fernanda" ,None,"F","Recife","Analista",9966.64],
    ["Ana"      ,19,"F","Belo Horizonte","Médico",2450.35],
    ["Eduardo"  ,43,"M","Belo Horizonte","Designer",9043.25],
    ["Eduardo"  ,26,"F","Salvador","Médico",13281.19],
    ["Gabriel"  ,62,"F","Porto Alegre","Vendedor",5584.73],
    ["Igor"     ,34,"F","Recife","Vendedor",1896.12],
    ["Igor"     ,36,"F","Rio de Janeiro","Designer",None],
    ["Eduardo"  ,44,"F","Curitiba","Engenheiro",8379.93],
    ["Bruno"    ,21,"M","Curitiba","Médico",12270.01],
    ["Daniela"  ,37,"F",None,"Médico",14848.64],
    ["Daniela"  ,63,"M","Recife","Analista",5364.56],
    ["Eduardo"  ,23,"M","Salvador","Vendedor",13079.54],
    ["Igor"     ,56,"M","São Paulo","Vendedor",7371.21],
    ["Carlos"   ,None,"F","Salvador","Médico",None],
    ["Eduardo"  ,57,"M","Belo Horizonte","Vendedor",11023.73],
    ["Bruno"    ,51,"M","Salvador","Designer",2558.1],
    ["Gabriel"  ,26,"F","São Paulo","Médico",10358.37],
    ["Bruno"    ,55,"M","São Paulo","Médico",6669.34],
    ["Fernanda" ,47,"F","Belo Horizonte","Médico",9319.39],
    ["Bruno"    ,61,"F","Rio de Janeiro","Professor",13486.26],
    ["Ana"      ,34,"F","Belo Horizonte","Analista",3986.32],
    ["Eduardo"  ,57,"F","Curitiba","Designer",11760.26],
    ["Helena"   ,65,"M","Belo Horizonte","Programador",7989.03],
    ["Gabriel"  ,43,"F","Curitiba","Engenheiro",7435.14],
    ["Ana"      ,44,"M","Belo Horizonte","Professor",7195.76],
    ["Daniela"  ,35,"F","Salvador","Analista",5377.26],
    ["Ana"      ,None,"F","Rio de Janeiro","Analista",None]
]

colunas1 = ["nome","idade","sexo","cidade","profissao","salario"]
df = pd.DataFrame(dados1, columns=colunas1)

#Output
print(f"Mediana dos valores ausentes:\n{df.fillna(df.median(numeric_only=True), inplace=True)}\n")

# === Questão 5 - Dado um DataFrame com a coluna estado_civil, escreva o código para ===
#                 aplicar One-Hot Encoding usando Pandas.

dados2 = [
    ['Daniela' ,    37, 'M'   , 'Porto Alegre'  ,   'Solteiro'      ,   'Médio'],
    ['Eduardo' ,    46, 'F'   , 'Curitiba'      ,   'Casado'        ,   'Médio'],
    ['Helena'  ,    31, 'F'   , 'São Paulo'     ,   'União Estável' ,   'Superior'],
    ['Juliana' ,    45, 'M'   , 'Curitiba'      ,   'União Estável' ,   'Médio'],
    ['Ana'     ,    62, 'M'   , 'São Paulo'     ,   'Solteiro'      ,   'Superior'],
    ['Gabriel' ,    34, 'F'   , 'Porto Alegre'  ,   'União Estável' ,   'Médio'],
    ['Igor'    ,    27, 'M'   , 'Porto Alegre'  ,   'Solteiro'      ,   'Superior'],
    ['Daniela' ,    33, 'F'   , 'Salvador'      ,   'Casado'        ,   'Médio'],
    ['Bruno'   ,    21, 'M'   , 'Curitiba'      ,   'União Estável' ,   'Superior'],
    ['Carlos'  ,    18, 'F'   , 'Salvador'      ,   'Solteiro'      ,   'Superior'],
    ['Fernanda',    19, 'M'   , 'São Paulo'     ,   'Casado'        ,   'Médio']
]

colunas2 = ['nome', 'idade', 'Sexo', 'Cidade', 'estado cívil', 'categoria escolar']
df = pd.DataFrame(dados2, columns=colunas2)

# -------------------------
# ONE HOT ENCODING - Transformando a coluna [estado cívil] em três colunas únicas - _Solteiro, _Casado, _União Estável
# e binarizando os resultado (0 e 1).
# -------------------------
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False).set_output(transform='pandas')
ohe_estado_civil = ohe.fit_transform(df[['estado cívil']])
df_estado_civil = pd.concat([df['nome'], ohe_estado_civil], axis=1)

# -------------------------
# LABEL ENCODER - Transformando as categorias escolares em hierárquias, resultando na binarização
# dos resultados.
# -------------------------
le = preprocessing.LabelEncoder()
le_cat_escolar = le.fit_transform(df['categoria escolar'])
df['categoria_escolar_label'] = le_cat_escolar

le_cat_escolar = pd.Series(le_cat_escolar, name='categoria escolar codificada') 
df_cat_escolar = pd.concat([df['nome'], le_cat_escolar],axis=1)

#Output
print(f'Questão 5 - Exemplo de One-Hot Enconding, concatenando nomes e estados cívis):\n{df_estado_civil}\n')
print(f'Questão 6 e 7 - Exemplo de Label Coding, concatenando nomes e categorias escolares:\n{df_cat_escolar}\nContagem de valores totais:{df['categoria_escolar_label'].value_counts()}\nOque prova que quando há uma hierárquia natural entre os valores, o Label Coding se faz necessário')