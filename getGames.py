import bs4 as bs
import urllib.request
import pandas as pd
from datetime import datetime
from datetime import timedelta
import pathlib

def start(path):
    #create URL
    today = datetime.today()
    url = "https://www.sports-reference.com/cbb/boxscores/index.cgi?month="+str(today.month)+"&day="+str(today.day)+"&year="+str(today.year)

    #load url HTML
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    gameList = []
    content = soup.find("div", {"id":"content"})
    section = content.find("div",{"class":"section_wrapper"})
    section_content = section.find("div",{"class":"section_content"})
    gameSummaries = section_content.find("div",{"class":"game_summaries"})
    games = gameSummaries.find_all("div",{"class":"game_summary nohover"})
    for game in games:
        table = game.find("table", {"class":"teams"})
        tbody = table.find("tbody")
        trs = tbody.find_all("tr")
        teams= []
        for tr in trs:
            a = tr.find("a")
            teams.append(a.text)
        gameList.append(teams)

    newfilePath = str(path) + "/csv/gameList.csv"

    df = pd.DataFrame(gameList)
    df.to_csv(newfilePath, float_format='%.2f', na_rep="NAN!")
