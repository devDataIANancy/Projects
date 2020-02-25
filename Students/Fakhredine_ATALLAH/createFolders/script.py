import os
import pandas as pd

columns = ['Prenom', 'Nom']
data = pd.read_csv('list.csv', names=columns)
fileName = data['Prenom']+"_"+data['Nom']
all_name = [name for name in fileName]
print(all_name)


for name in all_name:
    os.makedirs(name)
    with open(name+"/README.md", 'a'):
        os.utime(name)
