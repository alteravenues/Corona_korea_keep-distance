import pymysql
from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.db import connection
from django.template.context_processors import request

conn = pymysql.connect(host= "localhost", port=3307, user="root", password="0955", db="covid", charset="utf8")

#커서 가져오기
cursor=conn.cursor()
# sql 만들기
sql="select * from login"
cursor.execute(sql)

data_list=cursor.fetchall()


def index():
    sql="select * from login"
    cursor.execute(sql)
    data_list = cursor.fetchall()
    return render(request, 'corona/test.html',data_list=data_list)
conn.close()
