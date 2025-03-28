import pandas as pd

# upload do arquivo carros.csv
df = pd.read_csv('carros.csv')

# print head com 10 linhas
print(df.head(10))

# colunas do dataframe e index
#print(df.columns)
#print(df.index)

# sort descrescente pelo estado com maior qtde de carros
#print(df.sort_values("Quant Carros", ascending=False))

#Insira uma nova coluna com a proporçaõ de carros por estado

proporcao = df["Quant Carros"] /df["População do Estado"]
df["Carros por habitante"] = proporcao

print(proporcao)

filhos_por_regiao = df.groupby("Região")["Quant Carros Família com Filhos"].sum()
df["Carros_familia_filhos"] = filhos_por_regiao
print(filhos_por_regiao)


print(df.head)





# Boa noite  meu nome é Cristiana  faco parted a etapa 1 , que engloba o ETL , que é a extracao, transformacao e limpeza dos dados. 

# De Primeiro, para ter acesso ao dataset do desafio ultiliozamos a plataforma Kaggle, que é uma plataforma confiável.
# 
#  quando acessamos a pasta que acessamos do kaggle, observanos que havia 3 arquivos, sendo que avaliando melhor vimos que náo teria necessidade pois um dos tres ja havia os dados necessarios
# 
# Chegando nessa etapa , precisamos extrair os dados, e como fazer isso?
# 
#  Tivemos a opcao de subir no google drive para termos acesso a esse arquivo na nuvem, e deixamos a pasta publico para que todas tivessem acesso.

# E aprtir desse ponto ultilizamos o colab para comecar o desenvolvimento do Desafio.


# ultizamos a linguagem Python para importamos a biblioteca pandas e assim extrair  o arquivo. csv e dando sequencia no desenvolvimento do codigo.
#
# 

# Essa extração foi essencial para garantir um bom começo na análise e gerar insights mais precisos. Obrigado!"

