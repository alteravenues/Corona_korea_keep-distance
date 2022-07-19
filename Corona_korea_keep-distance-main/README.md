# 한림대학교 21년도 빅데이터 캡스톤디자인 팀 프로젝트

# 코로나19 통합 정보 제공 (covid-easy-check)
코로나 정보를 크롤링과 오픈API를 사용해 지역별 거리두기단계 및 방역수칙, 재난문자, 발생자수 확인, 내 위치 동선에 따른 재난문자 제공

 # 기획 의도
 ### “내가 방문할 곳의 코로나 거리두기 단계를 빠르고 정확하게 알려주는 곳은 왜 없을까?”
 라는 생각으로 프로그램 기획을 시작했습니다,  매번 헷갈리는 지역별 거리두기 단계와 거리두기 단계별 방역수칙은 물론, 추가 코로나 확진자 수와 관련뉴스, 세부적으로 알고 싶은 코로나 관련 정보들을 통합적으로 관리하는 서비스를 제공합니다.
# 제공 기능
1) 재난문자   
 현재의 재난문자 시스템은 내 위치에서 발령된 경보만을 받아옵니다. 현재로선 내가 지난주에 다녀온 “강릉”지역의 재난문자를 받아보고 싶다면 직접 검색하는 수밖에 없습니다.
 재난문자 API와 Geolocation, Geocode API를 사용해 GPS로 내가 다녀온 위치들을 저장하고, 같은 날짜 해당 지역에서 발령된 재난문자들을 알려줍니다. 또한 텍스트 검색으로 원하는 지역의 재난문자를 검색할 수 있습니다.

2) 코로나 캘린더   
 내가 갈 곳을 미리 등록하거나, 지나온 기록들을 달력에 기록합니다. 사용자가 늘어날 경우 데이터를 통해 0월0일, 해당 지역에 사람이 몰릴 것으로 예상이 가능합니다.

3) 코로나 거리두기 단계 및 방역수칙   
 크롤링을 사용해 지역별 거리두기 단계 및 방역수칙을 확인할 수 있습니다.

4) 코로나 확진자 수 확인   
 빅데이터 플랫폼의 오픈API를 통해 지역별, 전국 추가 확진자 수를 실시간으로 확인할 수 있습니다.

5) 코로나 뉴스   
 정확한 정보를 제공하는 뉴스를 크롤링하여 추가합니다.

6) 코로나 예측   
 FBProphet의 시계열 예측기법을 사용해 코로나 확진자 수를 예측합니다.

# 궁극적 목표
 내가 갈 지역의 날씨를 검색할 땐 손쉽게 날씨 앱을 켜서 지역을 검색합니다. 여러곳의 정보를 취합할 필요도 없습니다. 한 앱안에서 모든 구상이 가능합니다.
 날씨앱을 쉽게 검색하는 것처럼 **COSY CHECK**앱을 통해 가능한 많은 코로나 관련 정보를 깔끔한 UI로 사용자에게 쉽고 정확하게 전달하는 것이 궁극적인 목표입니다.

# 기술 스텍
<p align="left"></a> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> <a href="https://www.djangoproject.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-original.svg" alt="django" width="40" height="40"/> </a><a href="https://www.w3.org/html/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a>  <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> <a href="https://www.mysql.com/" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" alt="mysql" width="40" height="40"/>  <a href="https://git-scm.com/" target="_blank" rel="noreferrer"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> </p>
   
# 제작 진행일정
8월 ~ 9월 말  : 기능구현 및 웹서버 <br>
    ~ 10월 말 : UI 디자인 및 웹 완성 <br>
    ~ 11월 말 : 앱개발 완성<br>
    ~ 12월 중순: 사업계획작성 및 기능추가사항, 오류 수정<br>
    
# Contributors
### 김정웅  [Kim-JeongUng](https://github.com/Kim-JeongUng "Kim-JeongUng")   
- 팀장
- 코로나 정보, GPS, 확진자 수 등 크롤링 및 GPS, 역지오코딩 등 API활용, 텍스트 처리
- 코로나 확진자 수 예측 모델 개발
- 코드 방향성 리드
### 이화준  [Mython](https://github.com/MACE001 "Mython")    
- Django 기능 관리
- Html페이지 구성 및 url path 전담
- python-html간 연결   
### 김범수  [GanziMan](https://github.com/GanziMan "GanziMan")   
- Django 웹 프레임워크 전담
- 캘린더, 로그인 기능 구현
- 게시판 기능 구현
### 최홍석  [RednRock](https://github.com/RednRock "RednRock")   
- 경영 계획 및 전략 수립
- WBS 작성 및 서류 작성
- 뉴스 크롤링 및 오토 컴플리트 구현
### 박상범  [alteravenues](https://github.com/alteravenues "alteravenues")   
- CSS 전담
- 홈페이지 배치 전담
- 정보 탐색

# DEMO Scene
<img width="80%" src="https://user-images.githubusercontent.com/82865325/144747854-da05a52c-cc0a-43a2-b528-049bf2db08c7.png"/>
- 해당 지역 소분류 확진자 수 및 뉴스 크롤링, GPS인식, 지오코딩, 재난문자, 전국 확진자 수 API 사용
<br><br>
<img width="80%" src="https://user-images.githubusercontent.com/82865325/144001468-4a136716-062b-41ae-b10f-9b0631655268.png"/>
- 시계열 예측방식을 한 코로나 확진자 지수 예측


# View Video   
https://youtu.be/pSyxsR61Cks


# Use API 
- 행정안전부_재난문자방송 발령현황   
  https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=3058822
- 공공데이터활용지원센터_보건복지부 코로나19 시·도발생 현황   
  https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15043378
- 인터넷 접속 기반 GPS 좌표 찾기 (구글 Geolocation)   
  https://developers.google.com/maps/documentation/geolocation/overview
- GPS 좌표 기반 지역명 한글 변환 (카카오 역 지오코딩)   
  https://developers.kakao.com/product/map
	
# Crawling
- 지역별 거리두기 현황   
  http://ncov.mohw.go.kr/regSocdisBoardView.do?brdId=6&brdGubun=68&ncvContSeq=495
- 소단위 지역별 확진자 수   
  http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun=
  
# Use Open Source
- 캘린더 JS (추후 링크 추가 예정)
	
