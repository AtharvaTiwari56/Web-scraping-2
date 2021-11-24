import requests
from bs4 import BeautifulSoup
import time
import csv

START_URL = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
browser = requests.get(START_URL)
soup = BeautifulSoup(browser.text, 'html.parser')
star_table = soup.find_all('table')
temp_list  =[]
trs = star_table[7].find_all('tr')

for tr in trs:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td]
    temp_list.append(row)

Name = []
Distance =[]
Mass = []
Radius =[]
final_data = []

for i in range(1, len(temp_list)):
    Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

final_data = list(zip(Name, Distance, Mass, Radius))
with open("dwarfplanets.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerows(final_data)