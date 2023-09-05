print('Start van de scraping applicatie')

from bs4 import BeautifulSoup
import requests

pagina = requests.get("https://www.bitcoinmeester.nl/")
print(pagina.cookies)

html = BeautifulSoup(pagina.content, 'html.parser')

table = html.find('div')

btc = html.find(class_ = "muntbox")
print(btc)
# print(table.prettify())