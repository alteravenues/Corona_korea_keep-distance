import pandas as pd
# 메인 실행 파일
# 현재 실행순서 -> 신규 확진자, 누적확진자 -> 지역별 사회적 거리두기 단계 -> 내 지역 -> 내 지역 거리두기 단계 -> 신규확진자 및 누적확진자 -> 재난문자 -> 지역검색


# 일별, 전체 코로나 확진자수 API
# 전체 지역 누적확진자 및 추가확진자 getCovidKR(end_day, start_day)
# 전국 코로나 신규 확진자 CovidAll() 특정 지역 신규 확진자 CovidArea(area):
import CovidCount
import CovidCountSmallArea

# GPS API 및 이동 경로 엑셀 저장
import GPS_Reader_Saver

# 거리두기 단계 및 준수 수칙 크롤링
# 거리두기 단계 준수수칙 Junsu(level) 전체지역 코로나 단계 출력 KeepDistanceAllArea():
import KeepDistance

# 재난문자 API  #jenan_all(), jenan_area(area)
import JenanMessage

CovidCountSmallArea.CovidCountSave()

# 행정구역 엑셀읽어오기
df = pd.read_excel('행정구역.xlsx')
# 전체 코로나 상황 출력
CovidCount.CovidAll()

# 전체 지역별 단계 출력
KeepDistance.KeepDistanceAllArea()

# GPS 기반 내 지역 어딘지 출력
print(GPS_Reader_Saver.my_region2, GPS_Reader_Saver.my_region3)

# ** 시에서 시 빼주기 위해 슬라이싱
my_area = GPS_Reader_Saver.my_region2[:-1]

# 지역별 거리두기 단계 및 코로나 확진자 수, 재난문자 출력
while 1:
    do = df['시도명'].loc[df['시군구명'].str.contains(my_area) == True]
    dov = ""

    for val in do:
        dov = val

    for i in range(0, len(KeepDistance.area_level)):
        if len(my_area) < 2:
            print("데이터가 없습니다. 다시 검색하세요")
            break

        if KeepDistance.area_level[i].find("(" + my_area) != -1 or KeepDistance.area_level[i].find(", " + my_area) != -1:
            print(my_area, "지역은", i + 1, "단계 입니다.")
            KeepDistance.Junsu(i + 1)
            CovidCount.CovidArea(dov)
            JenanMessage.jenan_area(my_area)
            print(my_area,"지역 오늘 증가 수치 : ", CovidCountSmallArea.find(my_area))
            break

        elif i == len(KeepDistance.area_level) - 1:
            if dov == "":
                print("데이터가 없습니다. 다시 검색하세요")
                break
            else:
                print(my_area, "지역의 상급 행정구역", dov, "으로 검색됩니다. ")
                i = 0
                for j in range(0, len(KeepDistance.area_level)):
                    if KeepDistance.area_level[j].find("(" + dov) != -1 or KeepDistance.area_level[j].find(", " + dov) != -1:
                        print(my_area, "지역은", j + 1, "단계 입니다.")
                        KeepDistance.Junsu(j + 1)
                        CovidCount.CovidArea(dov)
                        JenanMessage.jenan_area(my_area)
                        print(my_area,"지역 오늘 증가 수치 : ", CovidCountSmallArea.find(my_area))
                        break

    print("\n지역을 입력하세요 : ")
    my_area = input()

