from csv import writer
from bs4 import BeautifulSoup
import requests


url = 'https://www.imdb.com/chart/top/'

page = requests.get(url)

print(page)
# If you get response [200-299] means successful

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find('tbody', class_ = 'lister-list').find_all('tr')

with open('imdb_movies_ranking.csv', 'w', encoding = 'utf8', newline = '') as f:
  thewriter = writer(f)
  header = ['Title', 'Year', 'Rating', 'Rank']
  thewriter.writerow(header)

  for list in lists:
    Title = list.find('td', class_ = 'titleColumn').a.text
    Year = list.find('td', class_ = 'titleColumn').span.text
    Rating = list.find('td', class_ = 'ratingColumn imdbRating').strong.text
    Rank = list.find('td', class_ = 'titleColumn').get_text(strip=True).split('.')[0]
# Try to understand and google on strip and split

    info = [Title, Year, Rating, Rank]
    print(info)
    thewriter.writerow(info)