import pandas as pd
from http import cookiejar
from bs4 import BeautifulSoup
import requests

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

response = requests.get('https://horse.hk33.com/race-results', cookies=cookies, headers=headers)
print(response.text)