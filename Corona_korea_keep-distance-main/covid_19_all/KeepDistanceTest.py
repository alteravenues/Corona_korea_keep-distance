# 거리두기 단계 및 준수 수칙 크롤링

import requests
from bs4 import BeautifulSoup

# 거리두기 단계 웹 크롤링
webpage = requests.get("http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495")
soup = BeautifulSoup(webpage.content, "html.parser")

area_level = [[], [], [], []]


# 거리두기 단계 별 방역수칙 웹 크롤링
KeepDistanceLevel = requests.get("http://ncov.mohw.go.kr/socdisBoardView.do?brdId=6&brdGubun=1")
KeepDistanceLevelSoup = BeautifulSoup(KeepDistanceLevel.content, "html.parser")


# 거리두기단계 준수수칙
def Junsu(level):

    print("\n", level, "단계 준수 수칙")
    #모임
    meet_level_list = KeepDistanceLevelSoup.select("#content > div > div:nth-child(3) > table > tbody > tr:nth-child(3) > td")
    #식당
    restaurant_level_list = KeepDistanceLevelSoup.select("#content > div > div:nth-child(7) > table > tbody > tr:nth-child(2) > td")
    #피시방
    pc_level_list = KeepDistanceLevelSoup.select("#content > div > div:nth-child(9) > table > tbody > tr:nth-child(24) > td")
    print(pc_level_list)
    if(len(pc_level_list)>4):
        pc_level_list.insert(0,  KeepDistanceLevelSoup.select("#content > div > div:nth-child(9) > table > tbody > tr:nth-child(24) > td")[0])
    print(pc_level_list)
    print(meet_level_list[0].text,": ",meet_level_list[level].text)
    if(level>=3):
        # 3단계, 4단계만 적용
        print(KeepDistanceLevelSoup.find(attrs={'class': 's_discript txt_ntc'}).text)
    print(pc_level_list[level].text)
    print(restaurant_level_list[level])
    print()

    '''test line'''
    '''    
    # 전체 구분 출력
    # 사회적 거리두기 단계별 수칙
    BasicDistanceSummary = KeepDistanceLevelSoup.select("#content > div > div:nth-child(3) > table > tbody > tr > td:nth-child(1)")
    for BD in BasicDistanceSummary:
        print(BD.text)
    print()

    # 1그룹시설에 대한 구분
    for C1 in KeepDistanceLevelSoup.select("#content > div > div:nth-child(5) > table > tbody > tr > td:nth-child(1)"):
        if (len(C1.text) < 10) and len(C1.text):
            print(C1.text)
        else:
            Category1Distance = ""
        #print(len(C1.text))
    print(Category1Distance)
    print()

    # 모든 구분 출력, 정리 필요
    print(KeepDistanceLevelSoup.select("#content > div > div > table > tbody > tr > td:nth-child(1)"))
    print()

    if len(pc_level_list) > 4:
        level = len(pc_level_list)
    '''

Junsu(1)

# 전체지역 코로나 단계 출력
def KeepDistanceAllArea():
    target = 4
    print(soup.find(attrs={'class': 'timetable'}).text + " 사회적 거리두기 단계\n\n")
    for descript in soup.find_all("p", "rssd_descript"):
        print(target, "단계")

        area_level[target - 1] = descript.text
        print(area_level[target - 1])

        target -= 1
        if target < 1:
            break
