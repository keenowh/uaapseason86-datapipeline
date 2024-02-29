from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from operator import attrgetter
from typing import TypedDict
import time
import csv

PATH = "C:/Program Files (x86)"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
matches = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    driver.get('https://uaapvolleyball.livestats.ph/tournaments/uaap-volleyball-season-86-women-s?')

    gamesList = driver.find_elements(By.CLASS_NAME, 'game-score')
    for game in gamesList:
        game.click()
        teamStats = []

        time.sleep(3)
        matchNo = game.find_element(By.CSS_SELECTOR, "span[class='typ-body-1-bold text-right']").text.split(' ')[1]

        tbodies = driver.find_elements(By.TAG_NAME, 'tbody')[2:]
        tbodyIndex = 0
        for tbody in tbodies:
            listOfPlayerRows = tbody.find_elements(By.TAG_NAME, 'tr')
            team_1_set = driver.find_element(By.ID, 'final-set-score').text.split((' - '))[0]
            team_2_set = driver.find_element(By.ID, 'final-set-score').text.split((' - '))[1]
            total_sets = int(team_1_set) + int(team_2_set)
            title = driver.find_elements(By.CLASS_NAME, 'typ-subheading-1')[tbodyIndex].text
            matchItem = {
                'team': title,
                'total_sets': total_sets,
                'playerStats': []
            }
            for player in listOfPlayerRows:
                playerStats = player.find_elements(By.XPATH, ".//td")
                indivPlayerItem = {
                    'player_no': playerStats[0].text.split(' ')[0],
                    'name': ' '.join(playerStats[0].text.split(' ')[1:]),
                    'att_won': playerStats[1].text,
                    'att_att': playerStats[2].text,
                    'block_won': playerStats[3].text,
                    'block_att': playerStats[4].text,
                    'serv_won': playerStats[5].text,
                    'serv_att': playerStats[6].text,
                    'dig_exc': playerStats[7].text,
                    'dig_att': playerStats[8].text,
                    'rec_exc': playerStats[9].text,
                    'rec_att': playerStats[10].text,
                    'set_exc': playerStats[11].text,
                    'set_att': playerStats[12].text
                }
                matchItem['playerStats'].append(indivPlayerItem)
            tbodyIndex += 1
            teamStats.append(matchItem)
        matchTitle = f"{teamStats[0]['team']} VS {teamStats[1]['team']}"
        match = {
            'matchNo': matchNo,
            'matchTitle': matchTitle,
            'teamStats': teamStats
        }
        matches.append(match)

        l = ""
        # for stat in playerStats:
        #     player = {
        #         'player_name': stat.text
        #     }
driver.quit()
with open('file.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    for match in matches:
        for teamPlayer in match['teamStats']:
            for player in teamPlayer['playerStats']:
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
                    match['matchTitle']
                ])
