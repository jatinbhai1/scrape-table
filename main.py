from bs4 import BeautifulSoup
import requests
from pprint import pprint
from html import unescape

response = requests.get(url='https://en.wikipedia.org/wiki/World_Bank')

soup = BeautifulSoup(response.text, 'html.parser')
table = soup.select(selector='table')
all_table_data = []
for _ in range(len(table)):

    if not soup.select(selector='table thead tr th'):
        thed = soup.select(selector='table tbody tr th')
        thead=[]
        for item in thed:
            if len(item.text) > 0:
                thead.append(item.text)
            elif len(item.text) == 0:
                thead.append(None)
    else:
        thed = soup.select(selector='table thead tr th')
        thead = []
        for item in thed:
            if len(item.text) > 0:
                too_append = unescape(item.text).replace(u'\n', '')
                thead.append(too_append.replace(u'\xa0', u''))
            elif len(item.text) == 0:
                thead.append(None)


    all_td = soup.select(selector='table tbody tr td')

    data = []

    for i in range(0, len(thead)):
        each_col=[]
        for k in range(i, len(all_td), len(thead)):
            if len(all_td[k].text)>0:
                to_append = unescape(all_td[k].text).replace(u'\n', '')
                each_col.append(to_append.replace(u'\xa0', u''))
            elif len(all_td[k].text)==0:
                each_col.append(None)
        data.append(each_col)
    dict ={}
    for d in range(len(thead)):
        dict[thead[d].replace('\n','')]=data[d]

    all_table_data.append(dict)


pprint(all_table_data[1])
