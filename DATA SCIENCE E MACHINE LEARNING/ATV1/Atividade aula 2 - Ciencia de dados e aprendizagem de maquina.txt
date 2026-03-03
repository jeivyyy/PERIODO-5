#Python
import pandas as pd

dados ={
    'Aluno': [
        'Lucas', 'Mariana', 'Pedro', 'Camila', 'Rafael',
        'Juliana', 'Thiago', 'Fernanda', 'Diego', 'Patricia',
        'Anderson', 'Bianca', 'Renato', 'Larissa', 'Victor'
    ],
    'Nota_Final': [
        8.5, 7.2, 6.8, 9.4, 5.9,
        10.0, 7.8, 6.0, 8.9, 7.0,
        4.5, 9.1, 6.3, 8.0, 7.6
    ],
    'Faltas': [
        3, 5, 7, 1, 10,
        0, 4, 12, 2, 6,
        14, 1, 9, 3, 5
    ]
}

df = pd.DataFrame(dados)
print(df)

# Questão 1 Mostre:Quantos alunos existem na base A média, maior e menor nota da turma
print("============================================")

quant = df['Aluno'].count()
print(f"Quantidade: {quant} alunos")

media = df['Nota_Final'].mean().round(2)
print(f"Média da turma: {media} pontos")

maior = df['Nota_Final'].max()
print(f"Maior nota: {maior} pontos")

menor = df['Nota_Final'].min()
print(f"Menor nota: {menor} pontos")


# Questão 2 Liste apenas os alunos aprovados por nota, considerando: Nota final maior ou igual a 7.0
print("============================================")

aprovados = df[df['Nota_Final']>= 7.0]
print(f"Aprovados:\n {aprovados[['Aluno', 'Nota_Final']]}")


# Questão 3 Liste os alunos reprovados por falta, considerando: Mais de 10 faltas
print("============================================")
turistas= df[df['Faltas'] >= 10]
print(f"Reprovados (por falta):\n {turistas[['Aluno', 'Faltas']]}")


# Questão 4 Crie uma nova coluna chamada Situacao, com a seguinte regra:"Aprovado" → Nota ≥ 7 e Faltas ≤ 10 "Reprovado" → Caso contrário
print("============================================")

df['Situacao'] = 'Reprovado'
df.loc[(df['Nota_Final'] >= 7.0) & (df['Faltas'] < 10), 'Situacao'] = 'Aprovado'
print(f"Aprovação da Turma:\n{df[['Aluno', 'Nota_Final', 'Faltas', 'Situacao']]}")

# Questão 5 (Desafio) Ordene o DataFrame: Da maior para a menor nota
print("============================================")

crescente = df.sort_values(by='Nota_Final', ascending=False)
print(f"Ordem de notas:\n {crescente}")