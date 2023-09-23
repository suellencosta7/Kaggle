
import pandas as pd

file_trains = pd.read_csv('test.csv')

num_passenger = file_trains['PassengerId']

print(len(num_passenger))