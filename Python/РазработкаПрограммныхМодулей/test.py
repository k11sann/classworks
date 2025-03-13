import requests
from bs4 import BeautifulSoup

url = 'https://minecraft-inside.ru/skins/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

print(r.status_code)

nickname = soup.find_all('h2', class_='box__title')
views = soup.find_all('div', class_='info__item post__views')

for i in range(len(nickname)):
    print(f"{nickname[i].text.strip()}; {views[i].text.strip()}")