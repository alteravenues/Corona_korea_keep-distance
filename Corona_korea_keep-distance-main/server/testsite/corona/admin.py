from django.contrib import admin
from .models import User,Event,Board#같은 경로의 models.py에서 User라는 클래스를 임포트하기

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','password') #관리자에서 볼 컬럼을 넣어주는 곳
admin.site.register(User,UserAdmin) # site에 등록
admin.site.register(Event)
admin.site.register(Board)