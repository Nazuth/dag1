import requests

results = requests.get('https://catfact.ninja/facts')

feitjes = results.json()
for feit in feitjes["data"]:
    print(feit["fact"])