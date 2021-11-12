import numpy as np
import requests
import datetime
aktie = "NOK"
def daten():
    url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol=' + aktie + '&apikey=EF0EJVHHUF3WO4QI'
    r = requests.get(url)
    global data
    data = r.json()
    #print(data)

daten()


name = data["Name"]
erwarteteskgv = data["ForwardPE"]
kgv = data["PERatio"]
kgwv = data["PEGRatio"]
kbv = data["BookValue"]
boerse = data["Exchange"]
land = data["Country"]
marketcap = data["MarketCapitalization"]
kompebit = data["EBITDA"]
perratio = data["PERatio"]
buchwert = data["BookValue"]
marge = data["ProfitMargin"]
zielanalyse = data["AnalystTargetPrice"]
jahreshigh = data["52WeekHigh"]
fivtymove = data["50DayMovingAverage"]
dividatum = data["DividendDate"]
dividende = data["DividendPerShare"]
sector = data["Sector"]
def einleitung():
    print(name)
    print(f"Die Börse: {boerse} .In flogendem Land: {land} . Das Unternehmen arbeitet in dem Sektor: {sector} .")
    print(f"Das Unternehmen besitzt eine Marktkapitalisierung von {marketcap} $. {name} schüttet am {dividatum} eine Dividende von {dividende} aus.")


def kgvanalyse():
    kgv_niedrig= "12"
    kgv_hoch ="20"
    if kgv >= kgv_niedrig:
        if kgv >= kgv_hoch:
            print(
                f"KGV ist überdurschnittlich groß. Die Aktie ist teuer. Achtung der Sektor {sector} ist möglicherweise ein Grund")
        else:
            print(
                f"KGV ist normal groß. Die Aktie ist fair bewertet. Achtung der Sektor {sector} ist möglicherweise ein Grund")
    else:
        print(f"KGV gering. Die Aktie ist preiswert bewertet. Achtung der Sektor {sector} ist möglicherweise ein Grund")


def kgwfanalyse():
    kgwv_hoch = "1"
    if kgwv > kgwv_hoch:
        print(
            f"Die Aktie ist wahrscheinlich überbewertet. Das KGWV beträgt {kgwv}. Achtung hier muss man auf das Wachstum und KGV achten.")
    elif kgwv == kgwv_hoch:
        print(
            f"Die Aktie ist Fair bewertet. Das KGWV beträgt {kgwv}. Der KGV im zusammenhang mit dem Wachstum stehen im Einklang.")
    else:
        print(
            f"Die Aktie ist wahrscheinlich unterbewertet. Das KGWV beträgt {kgwv}. Achtung hier muss man auf das Wachstum und KGV achten.")


def margeanalyse():
    prozentmarge= "0.04"
    if prozentmarge > "0.05":
        if prozentmarge >"0.10":
            print(f"Das Unternehmen hat eine enrom hohe Gewinnmarge von {prozentmarge}.")
        else:
            print(f"Das Unternehmen hat eine hohe Gewinnmarge von {prozentmarge}.")
    elif prozentmarge > "0":
        print(f"Das Unternehmen hat eine schwache Gewinnmarge von {prozentmarge}.")
    else:
        print(f"Das Unternehmen macht Verlusste in höhe von {prozentmarge}.")

def kursanalyse():
    url2 = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol='+ aktie +'&apikey=EF0EJVHHUF3WO4QI'
    h = requests.get(url2)
    aktuell = h.json()
    kurs = aktuell["Time Series (Daily)"]
    day = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yester = day - oneday
    aktuellerkurs= kurs[str(yester)]
    akkurs = aktuellerkurs["4. close"]
    if zielanalyse >= akkurs:
        print(f"Die Aktie hat Wachstumspotential. Die Differrenz zwischen Analystenschätzungen und dem aktuellen Kurswert liegt bei {round(np.double(zielanalyse)-np.double(akkurs))}USD$. Das wären {round(np.double(zielanalyse)/np.double(akkurs)*100-100)}%.")
    else:
        print(f"Die Aktie hat kein Wachstumspotential. Die Differrenz zwischen Analystenschätzungen und dem aktuellen Kurswert liegt bei {round(np.double(zielanalyse)-np.double(akkurs))}USD$, dass wärem {round(np.double(zielanalyse)/np.double(akkurs)*100-100)}%.")


    if akkurs >= jahreshigh:
        print(f"Die Aktie befindet sich im Moment auf einem 1 Jahres hoch und überschreitet diesen mit {round(np.double(jahreshigh)-np.double(akkurs))}USD$/, dass wären {round(np.double(jahreshigh)/np.double(akkurs)*100-100)}%.")
    else:
        print(f"Die Aktie ist {round(np.double(jahreshigh)-np.double(akkurs))}USD$ von dem 1 Jahres hoch entfernt, dass wären {round(np.double(jahreshigh)/np.double(akkurs)*100-100)}%. ")




einleitung()
kgvanalyse()
kgwfanalyse()
margeanalyse()
kursanalyse()