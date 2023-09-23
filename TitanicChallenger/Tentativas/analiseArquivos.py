# https://www.kaggle.com/code/alexisbcook/titanic-tutorial/notebook

import pandas as pd

file_trains = pd.read_csv('train.csv')
# print(file_trains)

file_trains['Survived'] = pd.to_numeric(file_trains['Survived'], errors= 'coerce')
# survived = (n for n in file_trains['Survived'] if n == 1)
survived = file_trains.loc[file_trains['Survived'] == 1]

female_survived = survived.loc[survived['Sex'] == 'female']  
male_survived = survived.loc[survived['Sex'] == 'male']

# df.loc[<linhas>, <colunas>]

sex_survive = survived.loc[survived['Survived'] == 1,['Survived','Sex']]
# typeKnow = survived['Cabin'][1]

sex_group =sex_survive.groupby(['Sex']).size()
# bairro_populacao.rename(columns={'População (2010)': 'populacao'}, inplace= True)

sex_group.index.values[0] = 'Mulheres'
sex_group.index.values[1] = 'Homens'



print(survived)

# sex_group.to_csv('sobreviventes_sexo.csv')




