from parameters import *
from bs4 import BeautifulSoup
import requests
import re
import datetime as dt
import pandas as pd
def horseracec33_soup(url):
    """
    Cookie for horserace33

    :param url: horserace33 url in parameter.py
    :return: bs4 obj
    """
    cookies = {
        'PHPSESSID': 'hjq4k3mump97adqb7he7p3jvq3',
        'lang': 'zh-hant',
        'client_browser_id': '787dc842-367d-4192-9562-9996765329a3',
        'SC_unique_748562': '0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'PHPSESSID=hjq4k3mump97adqb7he7p3jvq3; lang=zh-hant; client_browser_id=787dc842-367d-4192-9562-9996765329a3; SC_unique_748562=0',
        'Referer': 'https://horse.hk33.com/fixtures',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }
    resoponse = requests.get(url, cookies=cookies, headers=headers)
    soup=BeautifulSoup(resoponse.text,"html.parser")
    return soup
def race_date_catch(year):
    soup = horseracec33_soup(racedate_link + year)
    tr = soup.find("table", {"class": "ta_c mb_m mlr_a"})
    tr = tr.find_all("tr")
    racedate_list = []
    for i in tr:
        date = i.find_all("td")[0].a.string.strip().replace(" ", "")
        date = date[0:10]
        date = dt.datetime.strptime(date, "%Y-%m-%d")
        court = i.find_all("td")[1].span.string
        court = court_map[court]
        num_match = i.find_all("td")[3].a.string.strip().replace(" ", "").replace("場", "")
        track = i.find_all("td")[5].a.string.replace("跑道","").strip().replace(" ", "")
        if len(track)==0:
            track="AWT"
        # print(date)
        # print(num_match)
        # print(court)
        # print(track)
        temp_list = [date, num_match, court, track, year]
        racedate_list.append(temp_list)
    return racedate_list
def get_all_race_info():
    all_racedate_list = []
    for y in race_year:
        all_racedate_list.append(race_date_catch(y))
    all_racedate_list = [val for sublist in all_racedate_list for val in sublist]
    df = pd.DataFrame(all_racedate_list, columns=["date", "num_of_match", "court", "track", "season"])
    print(df)
    df.to_csv("./output/all_racedate_info.csv", index=False)

def get_single_day_result(date,num_match):
    url=f"https://horse.hk33.com/race-results/{str(date)}/{num_match}"
if __name__ == '__main__':
    get_all_race_info()
    pass
