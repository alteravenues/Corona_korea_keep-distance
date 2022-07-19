import requests
from bs4 import BeautifulSoup
import re

def Omicron():
    search ="http://ncov.mohw.go.kr/tcmBoardList.do?pageIndex=&brdId=3&brdGubun=&board_id=&search_item=1&search_content=%EA%B5%AD%EB%82%B4+%EB%B0%9C%EC%83%9D+%ED%98%84%ED%99%A9"

    req = requests.get(search)
    soup = BeautifulSoup(req.text, 'html.parser')
    title = soup.select("#content > div > div.board_list > table > tbody > tr:nth-child(1) > td.ta_l > a")
    st1 = str(title)
    pat = '\'\d{1,5}\''
    ref = re.findall(pat,st1)

    for i in range(0,len(ref)):
        ref[i]=ref[i].replace("\'", "")

    # 최신 국내 발생 현황 보도자료 링크
    Omiurl = "http://ncov.mohw.go.kr/tcmBoardView.do?brdId="+ref[0]+"&brdGubun="+ref[1]+"&dataGubun=&ncvContSeq="+ref[2]+"&contSeq="+ref[2]+"&board_id="+ref[3]+"&gubun=ALL"

    Omireq = requests.get(Omiurl)
    soup = BeautifulSoup(Omireq.text, 'html.parser')
    temp = soup.find_all('table', {'data-namose-item-id': 11})
    try:
        OmiCount = temp[0].select("p > span")[-1].text
    except:
        OmiCount = '12'

    return [Omiurl, OmiCount]
