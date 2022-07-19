from bs4 import BeautifulSoup
from selenium import webdriver

import openpyxl

def SaveGnews():
    news_num = 3  # 뉴스 개수 default 3
    wb = openpyxl.load_workbook('../server/testsite/corona/gnews.xlsx')

    while wb.active.max_row > 1:
        wb.active.delete_rows(2)

    returnroute = []
    driver = webdriver.Chrome("chromedriver")
    driver.get(
        'http://www.whosaeng.com/search.html?submit=submit&search=%EB%B0%A9%EC%97%AD%EB%8B%B9%EA%B5%AD&imageField3.x=0&imageField3.y=0&search_and=2&search_exec=all&search_section=sc1&news_order=1&search_start_day=&search_end_day=20211108')
    soup = BeautifulSoup(driver.page_source, "html.parser")

    temp = soup.find_all('div', {'class': 'search_result_list_box'})

    title = []
    msg = []
    url = []
    img = []
    for i in range(0, news_num):
        title.append(temp[i].select("dl > dt")[0])
        msg.append(temp[i].select("dl > dd.sbody > a")[0])
        try:
            img.append(temp[i].select("div.img_file>p>a>img")[0].get("src"))
        except:
            img.append(
            "https://user-images.githubusercontent.com/82865325/143685603-f168ff67-6f3d-425b-84d3-8b93d2b6a69a.png")
        url.append("http://www.whosaeng.com" + msg[i].get("href"))
        wb.active.append([img[i], title[i].text, msg[i].text, url[i]])
    wb.save('../server/testsite/corona/gnews.xlsx')

    return returnroute