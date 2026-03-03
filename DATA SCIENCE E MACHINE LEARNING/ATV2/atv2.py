# ATIVIDADE À SEGUIR CONTEMPLA: TODAS PARTE DOS EXERCÍCIOS SOBRE PANDAS DA AULA DO DIA 10/02 

import pandas as pd

vendas = {
    'Produtos': [
        'Notebook', 'Mouse', 'Teclado', 'Cadeira', 'Mesa', 'Monitor'
    ],
    'Categoria': [
        'Eletronicos', 'Eletronicos', 'Eletronicos', 'Móveis', 'Móveis', 'Eletronicos'
    ],
    'Quantidade': [
        2, 5, None, 1, 2, 3
    ],
    'Precos' : [
        3500, 80, 150, 900, None, 1200
    ],
    'Data': [
        '2024-01-10', '2024-01-12', '2024-01-15', '2024-01-20', '2024-01-22', None
    ]
}

clientes = {
    'Cliente': [
        'Ana', 'Bruno', 'Carla', 'Diego'
    ],
    'Idade': [
        28, 35, 22, 40
    ],
    'Cidade': [
        'São Paulo', 'Rio de Janeiro', 'São Paulo', 'Belo Horizonte'
    ],
    'Gasto_Total': [
        4200, 3800, 1500, 5200
    ]
}

df_vendas = pd.DataFrame(vendas)
df_clientes = pd.DataFrame(clientes)

# ========PARTE 1======== 
#1 - 
print(f"Produto com maior quantidade vendida: {df_vendas.loc[df_vendas['Quantidade'].idxmax(), 'Produtos']}\n")

#2 - 
print(f"Categoria de maior faturamento: {df_vendas.loc[df_vendas['Precos'].idxmax(), 'Categoria']}\n")

#3 -
print("Como tratar valores ausentes de preço?\n R = Substituindo pela média dos preços disponíveis\n")


#4 -
print("Oque é ticket médio? \n R = É uma média de gasto dos clientes.\n")

# ========PARTE 2======== 

print(f"Cinco primeiras linhas de cada Dataset:\nVendas:\n {df_vendas.head()}\nClientes:\n {df_clientes.head()}\n")

print(f"Tipos de dados de cada Dataset:\nVendas:\n {df_vendas.dtypes}\nClientes:\n {df_clientes.dtypes}\n")

print("Informações gerais [VENDAS]:")
df_vendas.info()
print("")
print("Informações gerais [CLIENTES]:")
df_clientes.info()
print("")

print(f"Quantas linhas e colunas no dataset Vendas:\n{df_vendas.shape}")
print(f"Quantas linhas e colunas no dataset Clientes:\n{df_clientes.shape}\n")

print(f"Quantas colunas possuem valores ausentes em Vendas:\n{df_vendas.isnull().sum()}")
print(f"Quantas colunas possuem valores ausentes em Clientes:\n{df_clientes.isnull().sum()}\n")

# ========PARTE 3======== 

eletronicos = df_vendas.loc[df_vendas['Categoria'] == 'Eletronicos']
print(f"Filtrar apenas produtos da categoria Eletronicos:\n{eletronicos}\n")

ppq = df_vendas[['Categoria', 'Produtos', 'Quantidade']]
print(f"Mostrar apenas as colunas:\n{ppq}\n")

max_preco = df_vendas[df_vendas['Precos'] >= 500]
print(f"Preços a partir de R$500,00:\n{max_preco}\n")

mean_preco = df_vendas['Precos'].fillna(df_vendas['Precos'].mean())
print(f"Substituir preço pela média:\n{mean_preco}\n")

sub_quant = df_vendas['Precos'].fillna(0)
print(f"Substituir por 0:\n{sub_quant}\n")

df_vendas['Data'] = df_vendas['Data'].fillna("Data não informada")
print(f"Preencher datas vazias:\n{df_vendas['Data']}\n")

df_vendas['Data'] = pd.to_datetime(df_vendas['Data'], errors='coerce')
print(f"Converter o tipo da coluna Data para datetime: \n{df_vendas['Data']}\n")

df_vendas['FaturamentoProduto'] = df_vendas['Precos'] * df_vendas['Quantidade']
faturamento_produto_total = df_vendas.groupby('Produtos')['FaturamentoProduto'].sum()
print(f"Faturamento total por Produto:\n{faturamento_produto_total}\n")

faturamento_categoria_total = df_vendas.groupby('Categoria')['FaturamentoProduto'].sum()
print(f"Faturamento total por Categoria:\n{faturamento_categoria_total}\n")

df_clientes['MediaGastos'] = df_clientes['Gasto_Total'].mean()
media_gasto_cidade = df_clientes.groupby('Cidade')['MediaGastos'].sum()
print(f"Média de gastos de clientes por cidade:\n{media_gasto_cidade}\n")

# ========DESAFIO FINAL========

top_produto = df_vendas.groupby('Produtos')['FaturamentoProduto'].sum().idxmax()
top_categoria = df_vendas.groupby('Categoria')['FaturamentoProduto'].sum().idxmax()
mean_ticket = df_clientes['Gasto_Total'].mean().round(2)

df_resumo = pd.DataFrame({
    'Produto mais vendido: ':[top_produto],
    'Categoria de maior faturamento: ': [top_categoria],
    'Ticket médio dos clientes: ': [mean_ticket]
})
print(f"Resumo de vendas:\n{df_resumo}")