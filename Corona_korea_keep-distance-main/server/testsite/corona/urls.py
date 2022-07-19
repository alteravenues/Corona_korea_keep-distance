from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    #main_pages
    path('', views.index, name='login'),
    path('news_page', views.news_page, name='login'),
    path('gnews_page', views.gnews_page, name='login'),
    path('pandj_page',views.patientjenan_page,name='login'),

    #func_links
    path('news/<str:query>',views.get_news,name="news"),
    path('gnews/',views.get_gnews,name="gnews"),
    path('gps/', views.get_gps, name="get_gps_value"),
    path('gps/<str:user_lng>/<str:user_lat>', views.get_location, name="get_location"),
    path('jenan/<str:area>',views.jenan,name="jenan"),
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('junsu/', views.junsu, name='login'),
    path('covid_value/<str:area>', views.covid_value, name='login'),
    path('patient/',views.covidpatient,name='patient'),
    #
    url(r'^event/new/$', views.event, name='event_new'),
    url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),
    path('lg/', views.users_login, name='lg'),
    path('logout/', views.users_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('index1/', views.index1, name='index1'),
    path('index2/', views.index2, name='index2'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('write/', views.write, name='write'),
    path('write/write_board', views.write_board, name='write_board'),
    path('<int:board_id>/create_reply', views.create_reply, name='create_reply'),
]