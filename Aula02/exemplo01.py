import pandas as pd

df_vendas = pd.read_excel('vendas_roupas.xlsx')
print(df_vendas)

print(f'\nQtde peças vendidas: {df_vendas['Unidades Vendidas'].sum()}')
print(f'\nMédia dos preços dos produtos: R$ {df_vendas['Preço por Unidade (R$)'].mean()}')
print(f'\nMaior valor de faturamento: R$ {df_vendas['Faturamento Total (R$)'].max()}')
print(f'\nMenor valor de faturamento: R$ {df_vendas['Faturamento Total (R$)'].min()}')

media_faturamento = df_vendas['Faturamento Total (R$)'].mean()
df_media = df_vendas[df_vendas['Faturamento Total (R$)'] > media_faturamento]
print(f'\nProdutos com faturamento acima da média:')
print(df_media)

df_alta = df_vendas[df_vendas['Satisfação'] == 'MUITO ALTO'] 
print(f'Produto com nível de satisfação muito alto')
print(df_alta)

df_baixo = df_vendas[df_vendas['Satisfação'] == 'BAIXO'] 
print(f'Produto com nível de satisfação baixo')
print(df_baixo)