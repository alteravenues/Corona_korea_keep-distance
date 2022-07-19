# 코로나 신규 확진자 확인

import requests
import xmltodict
import json
import datetime
import re
import pandas as pd
import os
BASE_DIR = os.getcwd()
# 데이터셋 : 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10&startCreateDt=20210809&endCreateDt=20210810'
# data.go.kr
from bs4 import BeautifulSoup

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
d1 = today.strftime("%Y%m%d")
d2 = d1 # yesterday.strftime("%Y%m%d")

url = 'http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey=tL8DvlXmKWq0V7ralHks5bdaNOVJ4Y1yMkYncaEWfjTO%2F3bobA%2FuSCSDuVBxesTC%2F3lbC8JcFJZJJe9j9GoPgQ%3D%3D&pageNo=1&numOfRows=10&'
payload = {'startCreateDt': d2, 'endCreateDt': d1, }
res = requests.get(url, params=payload)
if res.status_code == 200:
    result = xmltodict.parse(res.text)
    dd = json.loads(json.dumps(result))

df = pd.read_excel(str(BASE_DIR)+"\\corona\\행정구역.xlsx")
# 전체 지역 누적확진자 및 추가확진자
def getCovidKR():
    Covid = []
    # print('%s 기준' % (dd['response']['body']['items']['item'][0]["stdDay"]))

    i = len(dd['response']['body']['items']['item'])
    for area in dd['response']['body']['items']['item']:
        i -= 1
        Covid.append(dd['response']['body']['items']['item'][i]['gubun'])
        Covid.append(dd['response']['body']['items']['item'][i]['defCnt'])
        Covid.append(int(dd['response']['body']['items']['item'][i]['incDec']))
        return Covid

# 전국 코로나 신규 확진자
def CovidAll():
    Covid = []
    # print("%s기준 신규 확진자 및 누적 확진자" % (dd['response']['body']['items']['item'][0]["stdDay"]))
    print(dd)
    i = len(dd['response']['body']['items']['item'])

    for a in dd['response']['body']['items']['item']:
        i -= 1
        if dd['response']['body']['items']['item'][i]['gubun'].find("합계") != -1:
            Covid.append(dd['response']['body']['items']['item'][i]['incDec'])
            Covid.append(dd['response']['body']['items']['item'][i]['defCnt'])
            return Covid


# 도, 광역시, 특별시 지역 신규 확진자
def CovidArea(area):
    Covid = []
    do = df['시도명'].loc[df['시군구명'].str.contains(area) == True]
    dov = ""

    for val in do:
        dov = val
    i = len(dd['response']['body']['items']['item'])
    for a in dd['response']['body']['items']['item']:
        i -= 1
        if dd['response']['body']['items']['item'][i]['gubun'].find(dov) != -1:
            Covid.append(dd['response']['body']['items']['item'][i]['incDec'])
            Covid.append(dd['response']['body']['items']['item'][i]['defCnt'])
    return Covid,dov

today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
d1 = today.strftime("%Y%m%d")
d2 = d1 # yesterday.strftime("%Y%m%d")
# print("춘천 확진자 :{}".format(find("춘천")))
# print(CovidAll())




