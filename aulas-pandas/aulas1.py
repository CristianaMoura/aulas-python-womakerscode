import pandas as pd 



dados =  {
    'Nome': ['Max', 'Bella', 'Rocky', 'Luna'],
    'Raça': ['Labrador','Poodle', 'Boxer', 'Golden Retriever'],
    'Cor': ['Amarelo', 'Branco', 'Marrom', 'Dourado'],
    'Peso(kg)': [60, 35, 65, 55],
    'Altura(cm)': [30, 7, 28, 25],
    'Data de Nascimento': ['01/05/2018', '10/12/2019', '03/08/2017', '12/02/2016']
    }

# Criando um DataFrame
df_cachorros = pd.DataFrame(dados)
#print(df_cachorros.sort_values('Altura(cm)', ascending=False))
#print(df_cachorros[['Nome', 'Raça']])

is_boxer = df_cachorros[ 'Raça'] == 'Boxer'
is_marrom = df_cachorros['Cor'] == 'Marrom'

#print(df_cachorros[is_boxer & is_marrom])

is_marrom_ou_cinza = df_cachorros['Cor'].isin(['Marrom', 'Branco'])
#print(df_cachorros[is_marrom_ou_cinza])

df_cachorros['Altura(m)'] = df_cachorros['Altura(cm)'] / 100
print(df_cachorros)

df_cachorros.info()

dog_pequeno = df_cachorros[df_cachorros['Altura(m)'] <= 0.5]
dog_pequeno = dog_pequeno.sort_values('Altura(cm)', ascending=False)
dog_pequeno = dog_pequeno[['Nome', 'Altura(cm)', 'Peso(kg)']]
print(dog_pequeno)

print(df_cachorros.head())