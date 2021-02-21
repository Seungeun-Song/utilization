'''[조건]
1. 네이버에서 오늘 서울의 날씨정보를 가져온다
2. 헤드라인 뉴스 3건을 가져온다
3. IT 뉴스 3건을 가져온다
4. 해커스 어학원 홈페이지에서 오늘의 영어 회화 지문을 가져온다

[출력 예시]

[오늘의 날씨]
흐림, 어제보다 OO℃ 높아요
현재 OO℃  (최저 OO℃ / 최고 OO℃ )
오전 강수확률 OO% / 오후 강수확률 OO%

미세먼지 OO㎍/㎥ 좋음
초미세먼지 OO㎍/㎥ 좋음'''

import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"}

# [오늘의 날씨]
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EC%98%A4%EB%8A%98%EB%82%A0%EC%94%A8&tqi=hvcHvwprvTVsssyfcaZssssssHo-362008"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

weather = soup.find("div", attrs={"class":"weather_area _mainArea"})
degree = weather.find("span", attrs={"class":"todaytemp"}).get_text()
min_degree = weather.find("span", attrs={"class":"min"}).get_text()
max_degree = weather.find("span", attrs={"class":"max"}).get_text()
morning_rainfall = weather.find("span", attrs={"class":"point_time morning"}).find("span", attrs = {"class":"num"}).get_text()
afternoon_rainfall = weather.find("span",attrs={"class":"point_time afternoon"}).find("span",attrs={"class":"num"}).get_text()

dust = weather.find("dd", attrs={"class":"lv2"}).get_text()
ultra_dust = weather.find("dd",attrs={"class":"lv3"}).get_text()

print("[오늘의 날씨]")
print(weather.find("p",attrs={"class":"cast_txt"}).get_text())
print(f"현재 {degree}℃ (최저 {min_degree}℃ / 최고 {max_degree}℃ )")
print(f"오전 강수확률 {morning_rainfall}% / 오후 강수확률 {afternoon_rainfall}%", "\n")

print(f"미세먼지 {dust} ")
print(f"초미세먼지 {ultra_dust}","\n")



# [헤드라인 뉴스]
url = "https://news.naver.com/"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup= BeautifulSoup(res.text, "lxml")

news = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("div", attrs={"class":"hdline_article_tit"})
print("[헤드라인 뉴스]")
for idx, new in enumerate(news):
    if idx >= 3:
        break
    else:    
        print(idx+1+". ",new.get_text().strip())
        print("링크 : https://news.naver.com/"+ new.a["href"])
        print(" ")

# [IT 뉴스]
url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

it_news = soup.find("div", attrs={"class":"list_body newsflash_body"}).find_all("dt")

print("[IT 뉴스]")


for idx, new in enumerate(it_news):
    if idx >= 3:
        break
    elif new.a.get_text() == False:
        pass
    else:
        new.a.get_text()
        #title = new.a.get_text()
        # word = ["블록체인", "빅데이터","인공지능","비트코인","알고리즘","AI"]
        # if word in title:
        print(str(idx+1)+". ", new.a.get_text().strip())
        print("링크 : ", new.a["href"])
    




# [오늘의 영어 회화]

url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

conv= soup.find_all("div", attrs={"class":"conv_txtBox"})

print("[오늘의 영어 회화]","\n")
print("(영어지문)","\n", conv[1].get_text().strip())
print("(한글지문)","\n", conv[0].get_text().strip())