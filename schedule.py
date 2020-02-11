import bs4 as bs
import urllib.request
import pandas as pd
import random
import pathlib
import progressbar
import numpy as np

def schedule(names):
    schedule = [['YourScore', "OppScore","FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV","OppFGA","OppFGP","Opp3PA","Opp3PP","OppFTA","OppFTP","OppTRB","OppSTL","OppBLK","OppTOV"]]
    count = 1
    bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)
    for name in names:
        bar.update(count)
        try:
            url = 'https://www.sports-reference.com/cbb/schools/'+name+'/2020-gamelogs.html'
            source = urllib.request.urlopen(url).read()
            soup = bs.BeautifulSoup(source,'lxml')
            content = soup.find("div", {"id":"content"})
            all_sgl = content.find("div", {"id":"all_sgl-basic"})
            table_container_outer = all_sgl.find("div", {"class":"table_outer_container"})
            table_container = table_container_outer.find("div", {"id":"div_sgl-basic"})
            table = table_container.find("table", {"id":"sgl-basic"})
            tbody = table.find("tbody")
            trs = tbody.find_all("tr")
            count = count + 1
            for tr in trs:
                tds = tr.find_all("td")
                k = random.randint(0, 1)
                otherName = tds[2].text
                otherName = otherName.replace("&", "")
                otherName = otherName.replace(" ", "-", 5)
                otherName = otherName.replace(".", "") # decide on k once
                if k == 1:
                    if tds[1].text == "":
                        schedule.append([name, tds[4].text,otherName,tds[5].text,tds[7].text,tds[8].text,tds[10].text,tds[11].text,tds[13].text,tds[14].text,tds[16].text,tds[18].text,tds[19].text,tds[20].text, 1, tds[24].text,tds[25].text,tds[27].text,tds[28].text,tds[30].text,tds[31].text,tds[33].text,tds[35].text,tds[36].text,tds[37].text, 0])
                    else:
                        schedule.append([name,tds[4].text,otherName,tds[5].text,tds[7].text,tds[8].text,tds[10].text,tds[11].text,tds[13].text,tds[14].text,tds[16].text,tds[18].text,tds[19].text,tds[20].text, 0 ,tds[24].text,tds[25].text,tds[27].text,tds[28].text,tds[30].text,tds[31].text,tds[33].text,tds[35].text,tds[36].text,tds[37].text, 1])
                else:
                    if tds[1].text == "":
                        schedule.append([otherName,tds[5].text,name,tds[4].text,tds[24].text,tds[25].text,tds[27].text,tds[28].text,tds[30].text,tds[31].text,tds[33].text,tds[35].text,tds[36].text,tds[37].text, 0 ,tds[7].text,tds[8].text,tds[10].text,tds[11].text,tds[13].text,tds[14].text,tds[16].text,tds[18].text,tds[19].text,tds[20].text, 1])
                    else:
                        schedule.append([otherName,tds[5].text,name,tds[4].text,tds[24].text,tds[25].text,tds[27].text,tds[28].text,tds[30].text,tds[31].text,tds[33].text,tds[35].text,tds[36].text,tds[37].text, 1,tds[7].text,tds[8].text,tds[10].text,tds[11].text,tds[13].text,tds[14].text,tds[16].text,tds[18].text,tds[19].text,tds[20].text, 0])

        except AttributeError as e:
            #print(e)
            count = count + 1
        except IndexError as i:
            #print(i)
            count = count + 1
    return schedule


def scheduleStart(path):
    url = str(path) + '/csv/test.csv'
    names = ["teamName","GP","FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV","Home",'Away']
    data = pd.read_csv(url, names=names,encoding='utf-8')
    names = []

    data.replace('NAN!', np.nan, inplace = True)
    data = data.dropna()
    data = data.iloc[1:]
    for i in range(len(data)):
        names.append(data.iloc[i]['teamName'])

    schedules = schedule(names)
    url = str(path) + '/csv/test.csv'
    names = ['teamNames','number','1','2','3','4','5','6','7','8','9','10','homeATS','awayATS']
    data = pd.read_csv(url, names=names,encoding='utf-8')
    data = data.iloc[1:]
    teamNames = data['teamNames'].values.tolist()
    homeATS = data['homeATS'].values.tolist()
    awayATS = data['awayATS'].values.tolist()
    for game in schedules:
        team1 = game[0]
        team2 = game[2]
        for i in range(len(teamNames)):
            if team1 == teamNames[i]:
                if game[14] == 1:
                    game[14] = homeATS[i]
                if game[14] == 0:
                    game[14] = awayATS[i]
            if team2 == teamNames[i]:
                if game[25] == 1:
                    game[25] = homeATS[i]
                if game[25] == 0:
                    game[25] = awayATS[i]
    df = pd.DataFrame(schedules)
    df = df.drop([df.columns[2615] , df.columns[3271]], axis=0)
    labels = df.loc[:, [1,3]]
    df = df.drop([df.columns[0] , df.columns[1], df.columns[2], df.columns[3]] ,  axis='columns')
    df.to_csv(str(path) + '/csv/scheduleTest.csv', float_format='%.2f', na_rep="NaN")
    labels.to_csv(str(path) + '/csv/labels.csv', float_format='%.2f', na_rep="NaN")

