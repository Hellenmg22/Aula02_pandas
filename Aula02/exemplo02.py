import pandas as pd
import numpy as np

df_planilha_custos = pd.read_csv('planilha_de_custos.csv')
# print(df_planilha_custos.head(10))

# Totalizando a coluna custo
df_planilha_custos['Custo total (R$)'] = (
    df_planilha_custos['Preco de Compra (R$)'] +
    df_planilha_custos['Preco de Compra (R$)'] * df_planilha_custos['Imposto (%)'] / 100 +
    df_planilha_custos['Frete (R$)'] +
    df_planilha_custos['Taxa Operacional (R$)']
)

print(df_planilha_custos.head())

# Médias de Tendência Central
array_custo_total = np.array(df_planilha_custos['Custo total (R$)'])

# Média
media = np.mean(array_custo_total)

# Mediana
mediana = np.median(array_custo_total)

print('\nMédias de Tendência Central')
print(50*'-')
print(f'Média: {media}')
print(f'Mediana: {mediana}')

# Medidas de posição 
# Calculando o quartil

q1 = np.quantile(array_custo_total, 0.25)
q2 = np.quantile(array_custo_total, 0.50)
q3 = np.quantile(array_custo_total, 0.75)

print('\nMedidas de posição (Quartil)')
print(50*'-')
print(f'Q1: {q1}')
print(f'Q2: {q2}')
print(f'Q3: {q3}')

print('\nMenores')
print(50*'-')
df_menores = df_planilha_custos[df_planilha_custos['Custo total (R$)']] < q1

print('\nMaiores')
print(50*'-')
df_menores = df_planilha_custos[df_planilha_custos['Custo total (R$)']] > q3