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
for i in range(100000):
    num = i
    url = "https://www.football.org.il/en/players/player/?player_id={}&season_id=21".format(num)
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text,'html.parser')

    #static data scrape

    def player_id():
        """this function generate a random id for every player"""
        id = uuid.uuid4()
        return id

    def player_name():
        soup_name = soup.findAll("h1", {"class":"new-player-card_title"})
        name = str(soup_name)[35:-6]
        return name

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

    # def player_nationality():
    #     soup_nationality = soup.findAll("ul", {"class":"new-player-card_data-list"})
    #     soup_nationality = str(soup_nationality).split("<li>")[2]
    #     soup_nationality = soup_nationality.split("<")[2]
    #     soup_nationality = soup_nationality.split(">")[1]
    #     return soup_nationality

    def player_current_team():
        soup_team = soup.findAll("h2", {"class":"new-player-data_title js-container-title"})
        soup_team = str(soup_team).split("<span>")[1].split("\n")[1]
        return soup_team

    class player:

        def __init__(self, id, name, current_team):
            self.id = id
            self.name = name
            # self.nationality = nationality
            self.current_team = current_team
            # self.goals_current_season = goals_current_season
            # self.yellow_cards_current_season = yellow_cards_current_season

        # calculate the age
        def calculate_age(self, born):
            today = dt.date.today()
            # return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            self.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
            return self.age
            # print(self.age)

    def main():

        player_1 = player(player_id(), player_name(),player_current_team())
        player_1.calculate_age(player_birthdate())

        # to dataframe
        data = {
        'id': [player_1.id],
        'name': [player_1.name],
        'current_team': [player_1.current_team],
        'age': [player_1.calculate_age(player_birthdate())]
        }
        df = pd.DataFrame(data, columns = ['id','name','current_team','age'])
        df.to_excel("my_scout_result.xlsx")

    main()
