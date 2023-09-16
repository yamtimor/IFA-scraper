import bs4
import requests

response = requests.get('https://www.football.org.il/')
print(response.status_code)

robots = requests.get('https://www.football.org.il/robots.txt')
print(robots.text)