import pandas as pd
import csv
import difflib
import pathlib

def editList():
    #main path
    path = pathlib.Path(__file__).parent.absolute()
    #get todays games
    url = str(path) + "/csv/gameList.csv"
    names = ['team1', 'team2']
    gameList = pd.read_csv(url, names=names,encoding='utf-8')

    url = str(path) + "/csv/ATD data.csv"
    names = ['teamName',"FGA","FGP","3PA","3PP","FTA","FTP","TRB","STL","BLK","TOV", "HR", "AR"]
    teamData = pd.read_csv(url, names=names,encoding='utf-8')

    gameList = gameList.replace(' ', '-', regex=True)
    gameList['team1'] = gameList['team1'].str.lower()
    gameList['team2'] = gameList['team2'].str.lower()


    nameList = []
    for names in teamData.teamName:
        nameList.append(names)

    team1Location = []
    team2Location = []
    count = 0
    for games in gameList.team1:
        matches = difflib.get_close_matches(games, nameList)
        count = 0
        if matches != []:
            for names in teamData.teamName:
                if names != matches[0]:
                    count = count + 1
                else:
                    team1Location.append(count)
        else:
            team1Location.append(None)

    for games in gameList.team2:
        matches = difflib.get_close_matches(games, nameList)
        count = 0
        if matches != []:
            for names in teamData.teamName:
                if names != matches[0]:
                    count = count + 1
                else:
                    team2Location.append(count)
        else:
            team2Location.append(None)

    team1 = []
    for team in team1Location:
        if team == None:
            team1.append(None)
        else:
            team1.append([teamData.iloc[team]['teamName'],teamData.iloc[team]['FGA'],teamData.iloc[team]['FGP'],teamData.iloc[team]['3PA'],teamData.iloc[team]['3PP'],teamData.iloc[team]['FTA'],teamData.iloc[team]['FTP'],teamData.iloc[team]['TRB'],teamData.iloc[team]['STL'],teamData.iloc[team]['BLK'],teamData.iloc[team]['TOV'],teamData.iloc[team]['AR']])
    team2 = []
    for team in team2Location:
        if team == None:
            team2.append(None)
        else:
            team2.append([teamData.iloc[team]['teamName'],teamData.iloc[team]['FGA'],teamData.iloc[team]['FGP'],teamData.iloc[team]['3PA'],teamData.iloc[team]['3PP'],teamData.iloc[team]['FTA'],teamData.iloc[team]['FTP'],teamData.iloc[team]['TRB'],teamData.iloc[team]['STL'],teamData.iloc[team]['BLK'],teamData.iloc[team]['TOV'],teamData.iloc[team]['HR']])

    combined = []
    for i in range(len(team2Location)):
        if team1[i] == None:
            combined.append([None])
        elif team2[i] == None:
            combined.append([None])
        else:
            combined.append(team1[i] + team2[i])

    newfilePath = str(path) + '/csv/gamePrediction.csv'
    df = pd.DataFrame(combined)
    df.to_csv(newfilePath, float_format='%.2f', na_rep="NAN!")
