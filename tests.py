# # for web scraping
# import requests
# import bs4
#
# # for data proccessing
# import numpy as np
# import pandas as pd
# import os, glob, sys
# import re
# import time
# import datetime as dt
# import re
#
# # for generating ids
# import uuid
#
# # the scraping details
# res = requests.get("https://www.football.org.il/en/players/player/?player_id=23391&season_id=21")
# soup = bs4.BeautifulSoup(res.text,'html.parser')
#
# def player_current_team():
#     soup_team = soup.findAll("h2", {"class":"new-player-data_title js-container-title"})
#     soup_team = str(soup_team).split("<span>")[1].split("\n")[1]
#     print(soup_team)
#
# player_current_team()
