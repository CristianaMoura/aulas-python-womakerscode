import pandas as pd 
from matplotlib import  pyplot as plt
import numpy as np




df_concurso = pd.read_csv('dados_concurso.csv')
# print(df_concurso.head())


# print(df_concurso.columns)
# #print(df_concurso[df_concurso['Estado'] == 'PI'].count())



#print(df_concurso[['Número de Inscrição', 'Estado']].groupby('Estado').count())

# print(df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby(['Estado', 'Escolaridade']).count())

# print(df_concurso[ 'Deficiência'].value_counts(normalize = True)* 100)

# df_concurso2 = df_concurso.set_index(['Estado', 'Escolaridade'])
# print(df_concurso2.head(20))
# print(df_concurso2.loc[[('MS' ,'Ensino Médio'), ('CE', 'Ensino Superior')]])
# print(df_concurso2.sort_index())

# print(df_concurso.iloc[0:4, :4])

# print(df_concurso[['Número de Inscrição','Data de Nascimento', 'Nome']])



df_concurso['Data de Nascimento'] = pd.to_datetime(df_concurso['Data de Nascimento'])
df_concurso3 = df_concurso['Data de Nascimento'].loc[df_concurso['Data de Nascimento'] < pd.to_datetime('1995')]
df_concurso3 = df_concurso.loc[df_concurso['Data de Nascimento'] < pd.to_datetime('1995')]
#print(df_concurso3)

## usando plot graficos
# df_concurso.plot(x = 'Estado', y = 'Nome', kind = 'line') 
# plt.show()

# df_concurso4 = df_concurso.isna().any()## mostra se tem colunas com NAN
# df_concurso5 = df_concurso.isna().sum().plot(kind = 'bar')
# plt.show()## soma qts posicoes esta NAN


## df.dropna() ## remove todas as linhas com pelo menos um NaM.
## df. dropna(axis = 1) ## remove todas as colunas com pelo menos um NaN.
## df.dropna(subset = ['coluna1', 'coluna2']) ## remove linhas com NaN apenas nas colunas especificadas.
## df_ concurso.fillna(df_cachorros.median(numeric_only = truee)) ## substituindo valores nulos.
#print(df_concurso)  

print(df_concurso.isna())
print(df_concurso.fillna(np.median))



