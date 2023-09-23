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

for n in train_passId_list:
    if n in test_passId_list:
        test_survived.append(1)
    else:
        test_survived.append(0)

# DataFrame final
data_frame = pd.DataFrame({'PassengerId': test_passId_list, 'Test': 0})
print(data_frame)

data_frame.to_csv('Aquivo_FInal.csv')