from django.db import models
from django.urls import reverse


class User(models.Model):

    username = models.CharField(max_length=64,verbose_name='사용자명',default='')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm=models.DateTimeField(auto_now=True,verbose_name='등록시간')

    def __str__(self):
        return self.username

    class Meta:
        db_table='test_user'


class Event(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명', default='')
    title=models.CharField(max_length=200)
    description = models.TextField()
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    class Meta:
        db_table='cal_user'
    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title}</a>'
    @property
    def date1(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<a href="{url}"> {(self.end_time)-(self.start_time)}</a>'

class Board(models.Model):
    """
        title: 제목
        content: 내용
        author: 작성자
        like_count: 좋아요 카운트
        pub_date: 배포일
    """
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.CharField(max_length=100)
    like_count = models.PositiveIntegerField(default=0) # 양수입력 필드
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.title

class Reply(models.Model):
    """
        reply: Reply -> Board 연결관계
        comment: 댓글내용
        rep_date: 작성일
    """
    reply = models.ForeignKey(Board, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    rep_date = models.DateTimeField()

    def __str__(self):
        return self.comment
