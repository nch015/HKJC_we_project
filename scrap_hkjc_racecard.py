import pandas as pd
from http import cookiejar
from bs4 import BeautifulSoup
import requests
from dataclasses import fields,dataclass,field
from http.cookies import SimpleCookie
# Cookie: LocalRaceCardSetting=1%7C1%7C0%7C1%7C0%7C1%7C0%7C1%7C1%7C1%7C1%7C1%7C1%7C0%7C1%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C1%7C1; isEU=false; AMCV_06AB2C1653DB07AD0A490D4B%40AdobeOrg=-330454231%7CMCIDTS%7C19330%7CMCMID%7C31091660061109295092656485514540599232%7CMCAID%7CNONE%7CMCOPTOUT-1670065063s%7CNONE%7CvVersion%7C3.1.2%7CMCAAMLH-1670663368%7C3%7CMCAAMB-1670663368%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19252; LocalRaceCardDragTable=13%2F20; custProIn=; HKJCSSOGP=1670129937342; BotMitigationCookie_9518109003995423458="600428001670129982mZ+ZVDuAIbJeZ8ju5dxRQP3M2TE="; ASPSESSIONIDACRSDTSR=PAKHOBNBHICHDJMKMFCAGOEL
ccookies={'LocalRaceCardSetting': '1%7C1%7C0%7C1%7C0%7C1%7C0%7C1%7C1%7C1%7C1%7C1%7C1%7C0%7C1%7C1%7C0%7C0%7C0%7C0%7C1%7C1%7C0%7C1%7C1%7C1',
          'isEU': 'false',
          'AMCV_06AB2C1653DB07AD0A490D4B%40AdobeOrg': '-330454231%7CMCIDTS%7C19330%7CMCMID%7C31091660061109295092656485514540599232%7CMCAID%7CNONE%7CMCOPTOUT-1670065063s%7CNONE%7CvVersion%7C3.1.2%7CMCAAMLH-1670663368%7C3%7CMCAAMB-1670663368%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI%7CMCSYNCSOP%7C411-19252',
          'LocalRaceCardDragTable': '13%2F20',
          'custProIn': '',
          'HKJCSSOGP': '1670129937342',
          'BotMitigationCookie_9518109003995423458': '600428001670129982mZ+ZVDuAIbJeZ8ju5dxRQP3M2TE=',
          'ASPSESSIONIDACRSDTSR': 'PAKHOBNBHICHDJMKMFCAGOEL'}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'PHPSESSID=hjq4k3mump97adqb7he7p3jvq3; lang=zh-hant; client_browser_id=787dc842-367d-4192-9562-9996765329a3; SC_unique_748562=0',
    # 'Referer': 'https://horse.hk33.com/fixtures',
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
@dataclass
class hkjc_racecard:
    date:str=field(init=False)
    race_num:int=field(init=False)


response = requests.get('https://racing.hkjc.com/racing/information/Chinese/racing/RaceCard.aspx',cookies=ccookies,headers=headers)
print(response.status_code)
# print(response.text)
with open('output/racecard_html/04-12-2022_racecard.txt','w', encoding='UTF-8') as f:
    f.write(str(response.text))