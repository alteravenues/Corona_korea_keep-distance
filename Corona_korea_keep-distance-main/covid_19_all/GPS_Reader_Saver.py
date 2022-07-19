# GPS로 내 좌표 찾기 구글 geolocation api 사용
# 내 좌표로 지역 이름 한글화

import requests
#from dotenv import load_dotenv
import json

# 매일 GPS 기록 저장
import pandas as pd
import datetime
#load_dotenv(verbose=True)

#LOCATION_API_KEY = os.getenv('AIzaSyCArXnnrT7PhvZUinEuN94BRZfx5Qibyto')

# 좌표 찾기 api
url = f'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCArXnnrT7PhvZUinEuN94BRZfx5Qibyto'
data = {
    'considerIp': True,
}

result = requests.post(url, data).json()
my_lat = result["location"]["lat"]
my_lng = result["location"]["lng"]
# 임시 데이터 수원 장안동 좌표
#my_lat = 37.29088909058154
#my_lng = 127.00763359938911

# 좌표로 지역명 찾기 API
url = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=%s&y=%s"%(my_lng, my_lat)
headers = {"Authorization": "KakaoAK b3c7423bf62d904aad46bea35d6db181"} # API KEY
api_test = requests.get(url, headers=headers)
url_text = json.loads(api_test.text)

my_region2 = url_text['documents'][0]['region_2depth_name']
my_region3 = url_text['documents'][0]['region_3depth_name']


# GPS 기록저장

df = pd.read_excel('areaLog.xlsx', index_col =[0])

today = datetime.datetime.now()
today = today.strftime("%Y%m%d")

# 만약 마지막에 저장한 값과 달라질경우(지역의 이동 또는 날짜의 변경) 엑셀 저장
if not (df.iloc[-1]['my_region3'] == my_region3 or df.iloc[-1]['date'] == today):
    data ={
        'date': [today],
        'my_region2': [my_region2],
        'my_region3': [my_region3]
    }

    new_df = pd.DataFrame(data)

    # 이전 데이터와 새로운 데이터를 합침
    df = pd.concat([df,new_df])
    print("지역 또는 날짜가 바뀌어 데이터를 저장합니다.")
    df.to_excel('areaLog.xlsx')

print("lat : ",my_lat)

print("lng : ",my_lng)