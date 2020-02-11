import bs4 as bs
import urllib.request
import pandas as pd
import pathlib

#main path
def ATS():
    path = pathlib.Path(__file__).parent.absolute()
    urlHome = "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_home"
    urlAway = "https://www.teamrankings.com/ncb/trends/ats_trends/?sc=is_away"
    teamsHome = []
    teamsAway = []
    source = urllib.request.urlopen(urlHome).read()
    soup = bs.BeautifulSoup(source,'lxml')
    wrapper = soup.find("div", {"class": "wrapper"})
    div1 = wrapper.find("div", {"class": "content-wrapper clearfix"})
    mainWrapper = div1.find("div", {"class": "main-wrapper clearfix has-left-sidebar"})
    main = mainWrapper.find("main", {"role": "main"})
    table = main.find("table", {"class":"tr-table datatable scrollable"})
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        name = tds[0].find("a").text
        prec = tds[2].text
        teamsHome.append([name,prec])

    source = urllib.request.urlopen(urlAway).read()
    soup = bs.BeautifulSoup(source,'lxml')
    wrapper = soup.find("div", {"class": "wrapper"})
    div1 = wrapper.find("div", {"class": "content-wrapper clearfix"})
    mainWrapper = div1.find("div", {"class": "main-wrapper clearfix has-left-sidebar"})
    main = mainWrapper.find("main", {"role": "main"})
    table = main.find("table", {"class":"tr-table datatable scrollable"})
    tbody = table.find("tbody")
    trs = tbody.find_all("tr")
    for tr in trs:
        tds = tr.find_all("td")
        name = tds[0].find("a").text
        prec = tds[2].text
        teamsAway.append([name,prec])

    teamCombined = []
    for teamH in teamsHome:
        for teamA in teamsAway:
            if teamH[0] == teamA[0]:
                teamH[0] = teamH[0].replace(" ", "-", 3)
                teamH[1] = teamH[1].replace("%", " ")
                teamA[1] = teamA[1].replace("%", " ")
                if ("state" in teamH[0]) == False and ("State" in teamH[0]) == False:
                    teamH[0] = teamH[0].replace("-St", "-state")
                teamH[0] = teamH[0].replace("Ste-F-Austin", "stephen-f-austin")
                teamH[0] = teamH[0].replace("U-", "-university")
                if ("Upstate" in teamH[0]) == False:
                    teamH[0] = teamH[0].replace("-U", "-university")
                teamH[0] = teamH[0].replace("Beth-Cook", "bethune-cookman")
                teamH[0] = teamH[0].replace("Charl-South", "charleston-southern")
                teamH[0] = teamH[0].replace("Lg-Beach-state", "long-beach-state")
                teamH[0] = teamH[0].replace("-Cst", "-coast")
                teamH[0] = teamH[0].replace("-CC", "-corpus-christi")
                teamH[0] = teamH[0].replace("UCLA", "ucla")
                teamH[0] = teamH[0].replace("UMKC", "missouri-kansas-city")
                teamH[0] = teamH[0].replace("NJIT", "njit")
                teamH[0] = teamH[0].replace("-Tenn-", "-tennessee-")
                teamH[0] = teamH[0].replace("UAB", "alabama-birmingham")
                teamH[0] = teamH[0].replace("LA-Lafayette", "Lafayette")
                teamH[0] = teamH[0].replace("UCSB", "california-santa-barbara")
                teamH[0] = teamH[0].replace("Col-Charlestn", "college-of-charleston")
                teamH[0] = teamH[0].replace("Grd-Canyon", "grand-canyon")
                teamH[0] = teamH[0].replace("VCU", "virginia-commonwealth")
                teamH[0] = teamH[0].replace("Miss-", "mississippi-")
                teamH[0] = teamH[0].replace("Val-", "valley-")
                teamH[0] = teamH[0].replace("-mad", "-madison")
                teamH[0] = teamH[0].replace("CS-", "cal-state-")
                teamH[0] = teamH[0].replace("Fla-", "florida-")
                teamH[0] = teamH[0].replace("Geo-Wshgtn", "george-washington")
                teamH[0] = teamH[0].replace("LSU", "louisiana-state")
                teamH[0] = teamH[0].replace("VA-", "virginia-")
                teamH[0] = teamH[0].replace("GA-", "georgia-")
                teamH[0] = teamH[0].replace("NC-", "north-carolina-")
                teamH[0] = teamH[0].replace("SC-", "south-carolina-")
                teamH[0] = teamH[0].replace("TX-", "texas-")
                teamH[0] = teamH[0].replace("N-Mex", "new-mexico-")
                teamH[0] = teamH[0].replace("-Conn", "-connecticut-state")
                teamH[0] = teamH[0].replace("WI-Grn-Bay", "green-bay")
                teamH[0] = teamH[0].replace("Ark-Pine-Bl", "arkansas-pine-bluff")
                teamH[0] = teamH[0].replace("NW-", "northwestern-")
                teamH[0] = teamH[0].replace("N-", "north-")
                teamH[0] = teamH[0].replace("S-", "south-")
                teamH[0] = teamH[0].replace("SE-", "southeastern-")
                teamH[0] = teamH[0].replace("W-", "western-")
                if "virginia" in  teamH[0]:
                    teamH[0] = teamH[0].replace("western-", "west-")
                teamH[0] = teamH[0].replace("E-", "eastern-")
                teamH[0] = teamH[0].replace("Sw-", "southwest-")
                teamH[0] = teamH[0].replace("F-", "fairleigh-")
                teamH[0] = teamH[0].replace("-Grn", "-green")
                teamH[0] = teamH[0].replace("App-", "appalachian-")
                teamH[0] = teamH[0].replace("-Bap", "-baptist")
                teamH[0] = teamH[0].replace("Gard-Webb", "gardner-webb")
                teamH[0] = teamH[0].replace("Mass-Lowell", "massachusetts")
                teamH[0] = teamH[0].replace("Incar-Word", "incarnate-word")
                teamH[0] = teamH[0].replace("James-Mad", "James-madison")
                teamH[0] = teamH[0].replace("Loyola-Mymt", "loyola-marymount")
                teamH[0] = teamH[0].replace("Jksnville", "Jacksonville")
                teamH[0] = teamH[0].replace("WI-Milwkee", "milwaukee")
                teamH[0] = teamH[0].replace("IL-ilcago", "illinois-chicago")
                teamH[0] = teamH[0].replace("-Hrt", "-heart")
                teamH[0] = teamH[0].replace("-Hous", "-Houston")
                teamH[0] = teamH[0].replace("Middle-Tenn", "Middle-tennessee")
                teamH[0] = teamH[0].replace("Central-Mich", "Central-Michigan")
                teamH[0] = teamH[0].replace("florida-intl", "florida-international")
                if ("-Johns" in teamH[0]) == False:
                    teamH[0] = teamH[0].replace("St-", "saint-")
                teamH[0] = teamH[0].replace("BYU", "brigham-young")
                teamH[0] = teamH[0].replace("south-car-state", "south-carolina-upstate")
                teamH[0] = teamH[0].replace("AR-Lit-Rock", "arkansas-little-rock")
                teamH[0] = teamH[0].replace("Washingtn", "washington")
                teamH[0] = teamH[0].lower()
                teamH[0] = teamH[0].replace("florida-intl", "florida-international")
                teamH[0] = teamH[0].replace("la-", "louisiana-")
                if "uclouisiana-" in  teamH[0]:
                    teamH[0] = teamH[0].replace("uclouisiana-", "ucla")
                teamH[0] = teamH[0].replace("-fransco", "-francisco")
                teamH[0] = teamH[0].replace("(", "-")
                teamH[0] = teamH[0].replace(")", "")
                teamH[0] = teamH[0].replace("&", "")
                teamH[0] = teamH[0].replace("st-johns","st-francis-ny")
                teamH[0] = teamH[0].replace("central-fl","central-florida")
                teamH[0] = teamH[0].replace("albany","albany-ny")
                teamH[0] = teamH[0].replace("california-baptisttist","california-baptist")
                teamH[0] = teamH[0].replace("coastal-car","coastal-carolina")
                teamH[0] = teamH[0].replace("south-methodist","southern-methodist")
                teamH[0] = teamH[0].replace("tnorth-tech","louisiana-tech")
                teamH[0] = teamH[0].replace("saint-marys","saint-marys-ca")
                teamH[0] = teamH[0].replace("eastern-tennessee-state","east-tennessee-state")
                teamH[0] = teamH[0].replace("grambling-state","grambling")
                teamH[0] = teamH[0].replace("saint-fran--pa","saint-francis-pa")
                teamH[0] = teamH[0].replace("maryland-es","maryland-eastern-shore")
                teamH[0] = teamH[0].replace("sac-state","sacramento-state")
                teamH[0] = teamH[0].replace("mt-state-marys","mount-st-marys")
                teamH[0] = teamH[0].replace("southeast-missouri","southeast-missouri-state")
                teamH[0] = teamH[0].replace("south-illinois","southern-illinois")
                teamH[0] = teamH[0].replace("alab-am","alabama-am")
                teamH[0] = teamH[0].replace("boston-col","boston-college")
                teamH[0] = teamH[0].replace("south-mississippi","southern-mississippi")
                teamH[0] = teamH[0].replace("loyolouisiana-marymount","loyola-marymount")
                teamH[0] = teamH[0].replace("detroit","detroit-mercy")
                teamH[0] = teamH[0].replace("saint-bonavent","st-bonaventure")
                teamH[0] = teamH[0].replace("north-illinois","northern-illinois")
                teamH[0] = teamH[0].replace("-car-","carolina")
                teamH[0] = teamH[0].replace("geo-mason","george-mason")
                teamH[0] = teamH[0].replace("rob-morris","robert-morris")
                teamH[0] = teamH[0].replace("texas-pan-am","texas-pan-american")
                teamH[0] = teamH[0].replace("loyolouisiana-md","loyola-md")
                teamH[0] = teamH[0].replace("loyolouisiana-chi","loyola-il")
                teamH[0] = teamH[0].replace("louisiana-salle","la-salle")
                teamH[0] = teamH[0].replace("utah-valley-state","utah-valley")
                teamH[0] = teamH[0].replace("eastern-carolina","east-carolina")
                teamH[0] = teamH[0].replace("universitypenn","pennsylvania")
                teamH[0] = teamH[0].replace("=-universitypenn","pennsylvania")
                teamH[0] = teamH[0].replace("abl-christian","abilene-christian")
                teamH[0] = teamH[0].replace("north-iowa","northern-iowa")
                teamH[0] = teamH[0].replace("north-arizona","northern-arizona")
                teamH[0] = teamH[0].replace("central-ark","central-arkansas")
                teamH[0] = teamH[0].replace("western-virginia","west-virginia")
                teamH[0] = teamH[0].replace("wash-state","washington-state")
                teamH[0] = teamH[0].replace("illinois-chicago","il-chicago")
                teamH[0] = teamH[0].replace("youngs-state","youngstown-state") #174
                teamH[0] = teamH[0].replace("bowling-green","bowling-green-state") #102
                teamH[0] = teamH[0].replace("north-colorado","northern-colorado") #104
                teamH[0] = teamH[0].replace("cal-state-bakersfld","cal-state-bakersfield") #170
                teamH[0] = teamH[0].replace("--","-")
                #cal-state-bakersfld
                #cal-state-bakersfield
                teamCombined.append([teamH[0], teamH[1], teamA[1]])


    df = pd.DataFrame(teamCombined)
    df.to_csv(str(path) + '/csv/ATSrecords.csv', float_format='%.2f', na_rep="NAN!")
