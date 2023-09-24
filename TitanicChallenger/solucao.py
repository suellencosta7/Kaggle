import pandas as pd

train_file = pd.read_csv('TitanicChallenger/train.csv')
test_file = pd.read_csv('TitanicChallenger/test.csv')

# sobreviventes train
train_passId_survived = train_file[train_file['Survived'] == 1]

train_passId = train_passId_survived['PassengerId']
test_passId = test_file['PassengerId']

# Convertendo para listas
train_passId_list = list(train_passId)
test_passId_list = list(test_passId)

test_survived = []

id_passageiros_train = list(train_file['PassengerId']) 
condicao_sobreviventes_train = list(train_file['Survived'])

for n in test_passId_list:
    index = test_passId_list.index(n)
    if n in id_passageiros_train and condicao_sobreviventes_train[index] == 1 :
         test_survived.append(1)
    else:
        test_survived.append(0)






# DataFrame final
# data_frame = pd.DataFrame({'PassengerId': test_passId_list, 'Test': test_survived})clea
# print(data_frame)



# data_frame.to_csv('Aquivo_FInal.csv')





# Crie o DataFrame
