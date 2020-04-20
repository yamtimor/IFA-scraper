# for web scraping
import requests
import bs4

# for data proccessing
import numpy as np
import pandas as pd
import os, glob, sys
import re
import time
import datetime as dt
import re

import json

def player_name():
    soup_name = soup.findAll("h1", {"class":"new-player-card_title"})
    name = str(soup_name)[35:-6]
    return name

class player():

    def __init__(self, id, name):
        self.id = id
        self.name = name



df = pd.DataFrame(columns = ['id','name'])


def main():

    for i in range(10):
        id_player += 1
        url = "https://www.football.org.il/en/players/player/?player_id={}&season_id=21".format(id_player)
        res = requests.get(url)
        soup = bs4.BeautifulSoup(res.text,'html.parser')

        player = player(id_player, player_name())

        data = {player.id: player.name}
    print(data)

main()
