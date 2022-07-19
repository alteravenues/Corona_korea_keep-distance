
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.template import RequestContext

from django.db import connection
from corona.GPS_Reader_Saver import get_gps_value
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth import authenticate
from datetime import datetime,date,timedelta
from django.views import generic
from django.utils.safestring import mark_safe
from .models import Event
from .utils import Calendar
import calendar
from .forms import EventForm
from corona.GPS_Reader_Saver import get_gps_value
from corona.NewsCrawling_test import news
from corona.JenanMessage import jenan_area
from corona.governmentNews import gnews
from corona.KeepDistance import KeepDistanceAllArea,junsu
from corona.CovidCount import CovidAll,CovidArea
from corona.CovidCountSmallArea import find,find_danger,findLowDanger,findTopDanger
from corona.CovidPatientRoute import GetPatientRoute
# Create your views here.
from django.contrib import auth
from django.contrib import messages
# Create your views here.
from corona.Omicron import Omicron

def register(request):   #회원가입 페이지를 보여주기 위한 함수
    if request.method == "GET":
        return render(request, 'corona/register.html')
    elif request.method == "POST":
        username = request.POST.get('username',None)   #딕셔너리형태
        password = request.POST.get('password',None)
        re_password = request.POST.get('re_password',None)
        res_data = {}
        if not (username and password and re_password) :
            res_data['error'] = "모든 값을 입력해야 합니다."
            return render(request, 'corona/register.html',res_data)
        if password != re_password :
            # return HttpResponse('비밀번호가 다릅니다.')
            res_data['error'] = '비밀번호가 다릅니다.'
            return render(request, 'corona/register.html', res_data)
        else :
            user = User(username=username, password=make_password(password))
            user.save()
            return redirect(reverse('lg'))

def users_login(request):
    res_data={}

    if  request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(request,username=username, password=password)

        if user is not None:
            auth.login(request, user)
            request.session["username"] = username
            return redirect('/')
        else:
            res_data['error']='비밀번호가 달라요!'
    return render(request, "corona/user_login.html",{'error': 'Username or Password is incorrect.'})

def users_logout(request):
    logout(request)
    if request.method == 'POST':
        auth.logout(request)
        redirect('/')
    return redirect('/')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'corona/calendar.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()

    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('calendar'))
    return render(request, 'corona/event.html', {'form': form})



def get_news(request,query):#지역뉴스
    return HttpResponse(news(query))

def get_gnews(request):#정부뉴스
    return HttpResponse(gnews())

def jenan(request,area):
    return HttpResponse(jenan_area(area))

def covid_value(request,area):
    try:
        area = area.split(' ')[1]
    except:
        pass
    omicron = Omicron()
    try:
        korea = CovidAll()
        area1 = CovidArea(area)
        area2 = find(area)

        tds = """
                        <th>전국 누적확진자</th>
                        <th>전국 신규 확진자</th>
                        <th>{}도 신규확진자</th>
                        <th>{} 신규확진자</th>
                        <th>오미크론 누적 확진</th>
                        <tr>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td>{}</td>
                        <td><a href = '{}'>{}</td>
                        </tr>""".format(area1[-1],  # 도 단위
                                        area,  # 지역
                                        korea[1],  # 전체 누적확진자
                                        korea[0],  # 전체 신규확진자
                                        area1[0][0],  # 강원도 신규확진자
                                        area2,
                                        omicron[0],
                                        omicron[1])
    except:
        korea = "서버 점검중"
        area1 = "서버 점검중"
        area2 = "서버 점검중"
        tds = """
                        <th>전국 누적확진자</th>
                        <th>전국 신규 확진자</th>
                        <th>도단위 신규확진자</th>
                        <th>현재 지역 신규확진자</th>
                        <th>오미크론 누적 확진</th>
                        <tr>
                        <td>서버 점검중</td>
                        <td>서버 점검중</td>
                        <td>서버 점검중</td>
                        <td>서버 점검중</td>
                        <td><a href = '{}'>{}</td>
                        </tr>""".format(omicron[0],
                                        omicron[1])

    print(area2)

    #area2 = find(area)

    return HttpResponse(tds)


def index(request):
    context = {'find_top_danger': findTopDanger(), 'find_low_danger': findLowDanger()}
    if request.method == 'POST':
        k = ''
        k = request.POST.get("loca")
        context['k'] = k
    else:
        k = ''
        context['k'] = k
    print(context)
    return render(request,'corona/index.html',context=context)

def news_page(request):
    if request.method == 'POST':
        k = ''
        k = request.POST.get("loca")
        context = {
            'k': k
        }
        return render(request, 'corona/news_page.html', context=context)
    else:
        k = ''
        context = {
            'k': k
        }
        return render(request, 'corona/news_page.html', context=context)


def gnews_page(request):
    return render(request,'corona/gnews_page.html')

def index2(request):
    return render(request,'corona/index2.html')

def patientjenan_page(request):
    if request.method == 'POST':
        k = ''
        k = request.POST.get("loca")
        context = {
            'k': k
        }
        return render(request, 'corona/patientjenan_page.html',context=context)
    else:
        k = ''
        context = {
            'k': k
        }
        return render(request, 'corona/patientjenan_page.html',context=context)


def junsu(request):
    return HttpResponse(junsu(1))

def get_gps(request):
    return render(request,'corona/gps.js')

def covidpatient(request):
    return HttpResponse(GetPatientRoute())

def get_location(request,user_lng,user_lat):
    return HttpResponse(get_gps_value(user_lng,user_lat))

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import timezone
from django.urls import reverse
from django.core.paginator import Paginator
from .models import Board

def index1(request):
    all_boards = Board.objects.all().order_by("-pub_date")  # 모든 데이터 조회, 내림차순(-표시) 조회
    paginator = Paginator(all_boards, 5)
    page = int(request.GET.get('page', 1))
    board_list = paginator.get_page(page)

    return render(request, 'corona/index1.html', {'title': 'Board List', 'board_list': board_list})

def detail(request, board_id):
    board = Board.objects.get(id=board_id)
    return render(request, 'corona/detail.html', {'board': board})

def write(request):
    return render(request, 'corona/write.html')

def write_board(request):
    b = Board(title=request.POST.get('title'), content=request.POST.get('detail'), author="choi", pub_date=timezone.now())
    b.save()
    return HttpResponseRedirect(reverse('index1'))

def create_reply(request, board_id):
    b = Board.objects.get(id = board_id)
    b.reply_set.create(comment=request.POST['comment'], rep_date=timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(board_id,)))


def some_function():
    messages.add_message( messages.INFO, '정보를 나타냅니다.')

    # 축약된 방법
    messages.info('정보를 나타냅니다.')

