# 21-12-01 - 김정웅 selenium 사용
from bs4 import BeautifulSoup
from selenium import webdriver

import openpyxl
# 거리두기 단계 웹 크롤링

def SavePatientRoute():
    try:
        wb = openpyxl.load_workbook('../server/testsite/corona/PatientRoute.xlsx')

        while wb.active.max_row > 1:
            wb.active.delete_rows(2)

        returnroute = []
        driver = webdriver.Chrome("chromedriver")
        driver.get(
            'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=12&ncvContSeq=&contSeq=&board_id=&gubun=')
        soup = BeautifulSoup(driver.page_source, "html.parser")
        route = soup.select("#content > div > div.box_line2 > div > div > table > tbody > tr > td")
        for i in range(0, len(route), 1):
            route[i] = route[i].text.replace("소독완료", "").replace("\n", " ")

        wb.active.append([route[0], route[1], route[2], route[3], route[4]])
        wb.save('../server/testsite/corona/PatientRoute.xlsx')
        print("AA")

    except:
        pass

    return returnroute

SavePatientRoute()
#
# def GetPatientRoute():
#
# print(GetPatientRoute())
