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

# for generating ids
import uuid

# the scraping details
res = requests.get("https://www.football.org.il/en/players/player/?player_id=23391&season_id=21")
soup = bs4.BeautifulSoup(res.text,'html.parser')

def player_birthdate():
    # scrape and cleansing the dates
    soup_birth_date = soup.findAll("ul", {"class":"new-player-card_data-list"})
    birth_date = str(soup_birth_date).split("<li>")[1]
    birth_date = birth_date.split("<")[2]
    birth_date = birth_date.split(">")[1]
    bd_ls = []
    for i in birth_date.split("/"):
        if int(i) < 10:
            bd_ls.append("0"+str(i))
        else:
            bd_ls.append(str(i))

    birth_date = bd_ls[2]+"-"+bd_ls[0]+"-"+bd_ls[1]
    birth_date = dt.datetime.strptime(birth_date,"%Y-%m-%d")
    return birth_date


def calculate_age(born):
    today = dt.date.today()
    print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
    # print(today.year - born.year - ((today.month, today.day) < (born.month, born.day)))
    # print(self.age)


calculate_age(player_birthdate())
# def main():
#
#     fadida = player(player_id(), player_name())
#     fadida.calculate_age(player_birthdate())
#
# main()
