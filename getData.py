import bs4 as bs
import urllib.request
import pandas as pd
import csv
import pathlib
import progressbar

def getData():
    path = pathlib.Path(__file__).parent.absolute()
    urlFile = str(path) + '/csv/URLS.csv'
    URL = []
    with open(urlFile, 'r', encoding='utf-8') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            URL.append(row)
    data = []
    count = 0
    with progressbar.ProgressBar(max_value=352) as bar:
        for link in URL:
            bar.update(count)
            count = count + 1
            try:
                source = urllib.request.urlopen(link[0]).read()
                soup = bs.BeautifulSoup(source,'lxml')
                # title of the page
                div1 = soup.find("div", {"id": "all_team_stats"})
                div3 = div1.find("div", {"class": "overthrow table_container"})
                table = div3.find("table")
                tbody = table.find("tbody")
                trs = tbody.find_all("tr")
                td1 = trs[0].find_all("td")
                td2 = trs[2].find_all("td")
                teamName = link[0].replace("https://www.sports-reference.com/cbb/schools/", "")
                teamName = teamName.replace("/2020.html", "")
                #                                       "FGA",          "FGP",     "3PA",         "3PP",       "FTA",      "FTP",      "TRB",      "STL",          "BLK",          "TOV"
                data.append([teamName, td1[0].text, td1[3].text, td1[4].text, td1[9].text, td1[10].text, td1[12].text, td1[13].text, td1[16].text, td1[18].text, td1[19].text, td2[20].text])
            except AttributeError as e:
                print(e)
            except urllib.error.HTTPError as f:
                print(f)
        df = pd.DataFrame(data)
        list = df.values
        for i in range(len(list)):
            list[i][2] = float(list[i][2])/float(list[i][1])
            list[i][4] = float(list[i][4])/float(list[i][1])
            list[i][6] = float(list[i][6])/float(list[i][1])
        df = pd.DataFrame(list)
        df.drop(columns=[1])
        df.to_csv(str(path) + '/csv/data.csv', float_format='%.2f', na_rep="NAN!")
