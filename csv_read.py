print("Start met csv uitlees applicatie")

import pandas as pd

data = pd.read_csv("pokemon.csv")
print(data['Name'])

for r,rij in data.iterrows() :
    print("De naam van de pokemon is " + rij["Name"])

data2 = pd.read_json()    