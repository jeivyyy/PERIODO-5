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

while True: 
    resposta = int(input("================================\nEscolhas umas das opções a seguir:\n [0] - Sair\n [1] - Mostrar quantidade de alunos e médias de notas\n [2] - Lista de aprovação por notas\n [3] - Lista de reprovação do faltas\n [4] - Situação da turma\n [5] - Ordem de notas (crescente)\n"))
    match resposta:
        
        case 0: 
            print("Saindo. . .")
            break
        
        case 1:
            print(f"\nChamada:\n {df}\n")
            
            quant = df["Aluno"].count()
            print(f"Quantidade: {quant} alunos")
            
            media = df["Nota_Final"].mean().round(2)
            print(f"Média da turma: {media} pontos")
            
            maior = df['Nota_Final'].max()
            print(f"Maior nota: {maior} pontos")
            
            menor = df["Nota_Final"].min()
            print(f"Menor nota: {menor} pontos")
        
        case 2:
            aprovados = df[df['Nota_Final'] >= 7.0]
            print(f"\nAprovados\n: {aprovados[['Aluno', 'Nota_Final']]}")
        
        case 3: 
            turistas = df[df['Faltas'] >= 10]
            print(f"\nReprovados (por falta):\n {turistas[['Aluno', 'Faltas']]}")
        
        case 4:
            df['Situacao'] = 'Reprovado'
            df.loc[(df['Nota_Final']>= 7.0) & (df['Faltas'] < 10), 'Situacao'] = 'Aprovado'
            print(f"Aprovação da Turma:\n{df[['Aluno', 'Nota_Final', 'Faltas', 'Situacao']]}")

            
        case 5:
            crescente = df.sort_values(by='Nota_Final', ascending=False)
            print(f"\nOrdem de notas:\n {crescente}")   