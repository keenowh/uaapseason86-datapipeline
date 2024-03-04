from bs4 import BeautifulSoup
import requests
import csv

mainUrl = "https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s"

page = requests.get(mainUrl)
matchlinks = []
soup = BeautifulSoup(page.text, 'lxml')
game_matches = soup.findAll('a', class_ = 'game-score', href= True)
matches = []
totalGameMatch = len(game_matches)
for link in game_matches:
    if link.has_attr('href'):
        i = link['href'].split('/')
        matchlinks.append('https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s?game_id=' + i[4])

for url in matchlinks:
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'lxml')
    game = {
        'matchNo': totalGameMatch,
        'teamStats': []
    }
    teams = soup.findAll('tbody')[2:]
    teamIndex = 0
    for team in teams:
        teamName = soup.findAll('div', class_ = 'typ-subheading-1')[teamIndex].text.strip()
        matchNo = soup.findAll('span', class_ = 'typ-body-1-bold text-right')
        matchItem = {
            'teamName': teamName,
            'playerStats': []
        }

        players = team.findChildren('tr')
        for playerStatRow in players:
            playerStats = playerStatRow.findChildren('td')
            playerName = ' '.join(playerStats[0].text.strip().replace('  ', ' ').split(' ')[1:])
            if playerName.split(' ')[1] == 'Dongallo' or  playerName == 'Casley Monique Dongalio':
                playerName = 'Casley Monique Dongallo'
            indivPlayerItem = {
                'player_no': playerStats[0].text.strip().split(' ')[0],
                'name': playerName,
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
            matchItem['playerStats'].append(indivPlayerItem)

        game['teamStats'].append(matchItem)
        teamIndex += 1
    matches.append(game)
    totalGameMatch -= 1

with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for match in matches:
        for team in match['teamStats']:
            for player in team['playerStats']:
                writer.writerow([
                    player['player_no'],
                    player['name'],
                    player['att_won'],
                    player['att_att'],
                    player['block_won'],
                    player['block_att'],
                    player['serv_won'],
                    player['serv_att'],
                    player['dig_exc'],
                    player['dig_att'],
                    player['rec_exc'],
                    player['rec_att'],
                    player['set_exc'],
                    player['set_att'],
                    match['matchNo'],
                    team['teamName']
                ])

# storage_client = storage.Client()
#         bucket = storage_client.get_bucket(bucket_name)
#         blob = bucket.blob(destination_blob_name)
#         # Note the use of upload_from_string here. Please, provide
#         # the appropriate content type if you wish
#         blob.upload_from_string(data, content_type='text/csv')