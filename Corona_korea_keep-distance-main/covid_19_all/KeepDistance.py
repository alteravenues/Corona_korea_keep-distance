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

Distance = []


# 거리두기단계 준수수칙
def Junsu(level):
    print("\n", level, "단계 준수 수칙")

    if level == 1:
        Distance.append("""
        <article class="post">
          <header>
            <div class="title">
            </div>
         </header>
            <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>                  

      </article>
      """.format('(사적모임) 방역수칙을 준수하면서 인원제한 없음', '(스포츠 관람) 경기장 수용인원의 50% * 예방접종 완료자 제외', '(식당,카페) 운영 제한 없음',
                 '(노래방) 운영 제한 없음', '(PC방) 좌석 띄우기 없음', '(헬스장) 운영 제한 없음'))

    if level == 2:
        Distance.append("""<article class="post">
                  <header>
                    <div class="title">
                    </div>
                 </header>

            <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
              </article>""".format('(사적모임) 8명까지 사적모임 가능 * 예방접종 완료자 제외', '(스포츠 관람) 경기장 수용인원의 30% * 예방접종 완료자 제외',
                                   '(식당,카페)  24시 이후 포장ㆍ배달만 허용', '(노래방) 24시 이후 운영 제한',
                                   '(PC방) 좌석 한 칸 띄우기(단, 칸막이 있는 경우 좌석 띄우기 없음)', '(헬스장) 운영 제한 없음'))

    if level == 3:
        Distance.append("""<article class="post">
          <header>
            <div class="title">
            </div>
         </header>

            <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>

      </article>
      """.format('(사적모임) 접종 완료자 포함 최대 10명(미접종자 최대 4명)', '(스포츠 관람) 경기장 수용인원의 20% * 예방접종 완료자 제외',
                 '(식당,카페) 22시 이후 포장ㆍ배달만 허용', '(노래방) 22시 이후 운영 제한', '(PC방) 좌석 한 칸 띄우기(단, 칸막이 있는 경우 좌석 띄우기 없음)',
                 '(헬스장) 러닝머신 속도 6㎞ 이하 유지(고강도 유산소 운동→저강도 유산소 운동으로 대체), 샤워실 운영금지'))

    if level == 4:
        Distance.append("""<article class="post">
            <header>
              <div class="title">
              </div>
           </header>

           <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>
         <h1>{}</h1>

        </article>""".format('(사적모임) 접종 완료자 포함 최대 8명(미접종자 최대 4명)', '(스포츠 관람) 무관중 경기',
                             '(영화관) 22시 이후 운영 제한, 동행자 외 좌석 한 칸 띄우기',
                             '(PC방) 좌석 한 칸 띄우기(단, 칸막이 있는 경우 좌석 띄우기 없음), 22시 이후 운영 제한',
                             '(헬스장) 러닝머신 속도 6㎞ 이하 유지(고강도 유산소 운동→저강도 유산소 운동으로 대체), 샤워실 운영금지, 22시 이후 운영 제한'))

    return Distance


print(Junsu(3))


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
            
KeepDistanceAllArea()
