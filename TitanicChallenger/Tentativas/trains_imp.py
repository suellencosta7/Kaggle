import pandas as pd

file_trains = pd.read_csv('TitanicChallenger/train.csv')
file_trains['Survived'] = pd.to_numeric(file_trains['Survived'], errors= 'coerce')
survived = file_trains.loc[file_trains['Survived'] == 1]
list_survived = survived['PassengerId']



# print(list_survived)

def listPasserId ():

    """ Retorna a lisra de sobreviventes do df trains"""

    frame_list = []
    for n in list_survived:
        frame_list.append(n)

    return frame_list

chamada_teste = listPasserId()

print(type(survived))