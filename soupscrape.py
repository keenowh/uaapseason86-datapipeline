from bs4 import BeautifulSoup
import requests

mainUrl = "https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s"

page = requests.get(mainUrl)
matchlinks = []
soup = BeautifulSoup(page.text, 'lxml')
game_matches = soup.findAll('a', class_ = 'game-score', href= True)

for link in game_matches:
    if link.has_attr('href'):
        i = link.decode_contents()
        matchlinks.append('https://uaapvolleyball.livestats.ph' + link['href'])
        l = ''

for url in matchlinks:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    