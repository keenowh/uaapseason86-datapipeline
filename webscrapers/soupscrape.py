from bs4 import BeautifulSoup
import requests

mainUrl = "https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s"

page = requests.get(mainUrl)
matchlinks = []
soup = BeautifulSoup(page.text, 'lxml')
game_matches = soup.findAll('a', class_ = 'game-score', href= True)

for link in game_matches:
    if link.has_attr('href'):
        i = link['href'].split('/')
        matchlinks.append('https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s?game_id=' + i[4])

for url in matchlinks:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')

    teams = soup.findAll('tbody')[2:]

    for team in teams:

        teamMatchStat = []

        players = team.findChildren('tr')
        for playerStatRow in players:
            playerStats = playerStatRow.findChildren('td')
            indivPlayerItem = {
                'player_no': playerStats[0].text.strip().split(' ')[0],
                'name': ' '.join(playerStats[0].text.strip().replace('  ', ' ').split(' ')[1:]),
                'att_won': playerStats[1].text.strip(),
                'att_att': playerStats[2].text.strip(),
                'block_won': playerStats[3].text.strip(),
                'block_att': playerStats[4].text.strip(),
                'serv_won': playerStats[5].text.strip(),
                'serv_att': playerStats[6].text.strip(),
                'dig_exc': playerStats[7].text.strip(),
                'dig_att': playerStats[8].text.strip(),
                'rec_exc': playerStats[9].text.strip(),
                'rec_att': playerStats[10].text.strip(),
                'set_exc': playerStats[11].text.strip(),
                'set_att': playerStats[12].text.strip()
            }
            teamMatchStat.append(indivPlayerItem)

            l = ''



        # for
             # .findChildren("a", recursive=False))



    