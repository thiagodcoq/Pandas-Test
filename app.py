import pandas as pd
import re


df = pd.read_csv('pokemon_data.csv')
# print(df.tail(3))

## Read Headers

# df.columns

## Read each Column

# print(df[['Name','Type 1','HP']][0:5])

## Read each Row

# print(df.iloc[1:4])

# for index,row in df.iterrows():
    # print(index,row['Name'])

## Read a specific location (R,C)

# print(df.iloc[2,1])

# print(df.loc[df['Type 1'] == "Fire"])

# print(df.describe())

# print(df.sort_values('Name',ascending=False))

# print(df.sort_values(['Type 1','HP'],ascending=[True,False]))

## Making changes to the data

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']

# df = df.drop(columns=['Total'])

# print(df.sort_values(['Total'],ascending=False))

#df['Total'] = df.iloc[:,4:10].sum(axis=1) # axis=1 horizonta / axis=0 vertical

#cols = list(df.columns.values)
#df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

# print(df.head(5))

## Saving data

#df.to_csv('new.csv', index=False)  # index=False é pra nao salvar o index no csv

# df.to_excel('new.xlsx', index=False)

# df.to_csv('new.txt', index= False, sep='\t') # sep=\t pra separa em TAB

## Filtering Data


# new_df=df.loc[(df['Type 1'] =='Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# new_df=new_df.reset_index(drop=True)  #drop=True tira o index anterior, 
# print(new_df)
# print(df.loc[df['Legendary'] == True]) 

# print(df.loc[df['Name'].str.contains('Mega')])
# print(df.loc[~df['Name'].str.contains('Mega')])    # o ~ signifca not, tipo o ! do C

#print(df.loc[df['Type 1'].str.contains('fire|grass',flags=re.I,regex=True)])
# importei a "re", que tem essa funcao regex que valida ou desvalida a expressao anterior chamada por str.contais() e o flags=re.I ignora letra maiuscula.

#print(df.loc[df['Name'].str.contains('^pi[a-z]*',flags=re.I,regex=True)]) 
# Mostrar apenas os pokemons com nome comecando com "pi". o ^ indica inicio da string e o * é pra considera os que tem 0 ou mais do que está entre []

## Conditional changes

# df.loc[df['Type 1'] == 'Fire','Type 1'] = 'Fogo'  #Muda fire pra fogo
# print(df.head(10))
# df.loc[df['Type 1'] == 'Fogo','Type 1'] = 'Fire'  #Muda de volta
# print(df.head(10))

# df.loc[df['Type 1'] == 'Fire', 'Legendary'] = True  # if type1==fire: legendary=True

# df.loc[df['HP'] > 60, ['Generation','Legendary']] = ['Tank', 'Test 1']  # if hp>50: generation= tank and legendary=test 1
#print(df)

## Aggregate Statistics (GROUPBY)

#print(df.groupby(['Type 1']).mean(numeric_only=True).sort_values('Defense',ascending=False))  
# essa groupby agrupa nesse ex o Type, e a funcao .mean faz a media de todos os stats por tipo e dps da sort pra ver a maior defesa

#print(df.groupby(['Type 1']).sum(numeric_only=True)) #soma todos os status por tipo, se eu tirar op numeric_only ele concatena as string
#print(df.groupby(['Type 1']).count())
# df['count']=1
# print(df.groupby(['Type 1']).count()['count']) #criei a coluna count q é 1 pra todos os pokemons, e na count contei so ela como fosse um soma++ 
# print(df.groupby(['Type 1','Type 2']).count()['count']) #contar os tipos secundarios  de cada tipo


