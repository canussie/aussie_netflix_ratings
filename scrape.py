#!/usr/bin/python

import requests
import re
from bs4 import BeautifulSoup


def getshowlist():
    url = "https://www.finder.com.au/netflix-tv-shows"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', class_="ts-table-container")

    tb = div.find('table', class_='luna-table')
    #print tb

    list = {}

    for row in tb.find_all('tr'):
        #print row
        name = row.find('b')
        year = row.find("td", {"data-title": "Year of release"})
        temp = str(name)
        temp2 = str(year)
        #print type(name)
        title = re.sub('<[^<]+?>', '', temp)
        release = re.sub('<[^<]+?>', '', temp2)
        #print title, release
        list[title] = release
    return list
