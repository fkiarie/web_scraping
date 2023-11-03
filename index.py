import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)

#print(page.text)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id="ResultsContainer")

print(results.prettify())