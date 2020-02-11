import pandas as pd
import numpy as np
import pathlib

#main path
def func():
    path = pathlib.Path(__file__).parent.absolute()
    url = str(path) + '/csv/ATSrecords.csv'
    names = ['number','teamNameATS', 'homeATS', 'awayATS']
    ATS = pd.read_csv(url, names=names,encoding='utf-8')
    url = str(path) + '/csv/data.csv'
    names = ["teamNameData", "GP","FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV"]
    data = pd.read_csv(url, names=names,encoding='utf-8')

    
    data = data.iloc[1:]
    ATS = ATS.iloc[1:]
    ATS = ATS.drop('number', 1)

    teamNameATS = ATS['teamNameATS'].tolist()
    teamNameData = data['teamNameData'].tolist()

    ATSdata = ATS.values.tolist()
    teamData = data.values.tolist()
    nonNames = []
    for name in teamNameATS:
        for i in range(len(teamNameData)):
            if name == teamNameData[i]:
                teamData[i].append(ATSdata[i][1])
                teamData[i].append(ATSdata[i][2])
                break

    df = pd.DataFrame(teamData)
    df = df.iloc[:, :-2]
    df.to_csv(str(path) + '/csv/test.csv', float_format='%.2f', na_rep="NAN!")
func()
