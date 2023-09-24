import pandas as pd

train_file = pd.read_csv('TitanicChallenger/train.csv')
test_file = pd.read_csv('TitanicChallenger/test.csv')


id_passageiros_train = list(train_file['PassengerId']) 
condicao_sobreviventes_train = list(train_file['Survived'])
test_passId_list = list(test_file['PassengerId']) 


test_survived = []


for n in test_passId_list:
    index = test_passId_list.index(n)
    if n in id_passageiros_train and condicao_sobreviventes_train[index] == 1 :
         test_survived.append(1)
    else:
        test_survived.append(0)



data_frame = pd.DataFrame({'PassengerId': test_passId_list, 'Test': test_survived})

print(data_frame)