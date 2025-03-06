import requests
from bs4 import BeautifulSoup

url = 'https://dzen.ru/?'
response = requests.get(url)

request_result=requests.get(url) 
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup)
articles = soup.find_all('a', class_='dzen-desktop--card-top-avatar__rootElement-Us')
print(articles)
print(request_result.status_code)
for article in articles:
    print(article.text.strip())