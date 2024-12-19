import pandas as pd

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

df['Total'] = df.iloc[:,4:10].sum(axis=1) # axis=1 horizonta / axis=0 vertical

cols = list(df.columns.values)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]

print(df.head(5))

## Saving data

df.to_csv('new.csv', index=False)  # index=False é pra nao salvar o index no csv

# df.to_excel('new.xlsx', index=False)

# df.to_csv('new.txt', index= False, sep='\t') # sep=\t pra separa em TAB


