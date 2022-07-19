# 정부 뉴스
import openpyxl
import os
BASE_DIR = os.getcwd()
import os

BASE_DIR = os.getcwd()
def gnews():
    wb = openpyxl.load_workbook(str(BASE_DIR)+"\\corona\\gnews.xlsx",data_only=True)
    result =""
    cnt = 0

    for i in wb.active.rows:
        if cnt > 0:
            result += ("<article class='mini-post'><header>")
            result += ('<a href="{}"><img src="{}" alt="" />'.format((i[3].value),i[0].value))
            result += ("<h3>{}<h3>".format(i[1].value))
            result += ("<h3>{}<h3></a>".format(i[2].value))

            result += ("</header></article>")
        cnt += 1
    if cnt == 0:
        result+=("<h3>None<h3> \n")

    return result
