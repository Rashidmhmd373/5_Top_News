import requests
from bs4 import BeautifulSoup

def get_news():
  """Gets the top 5 news headlines from the BBC News website."""

  url = 'https://www.bbc.com/news'
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')

  headlines = soup.find('body').find_all('h3')
  return headlines[:5]

def print_news(headlines):
  """Prints the top 5 news headlines."""

  for headline in headlines:
    print(headline.text.strip())

if __name__ == '__main__':
  headlines = get_news()
  print_news(headlines)
