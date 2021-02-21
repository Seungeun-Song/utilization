import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hv4aTsp0JXVsslE0lFhssssss%2FZ-290408"
    soup = create_soup(url)
    # 흐림, 어제보다 OO℃ 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    # 현재 OO℃  (최저 OO℃ / 최고 OO℃ )
    curr_temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨", "") # replace 함수로 필요없는 것 공백으로 대체
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    # 오전 강수확률 OO℃ / 오후 강수확률 OO℃ 
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    # 미세먼지 OO㎍/㎥ 좋음
    # 초미세먼지 OO㎍/㎥ 좋은
    dust = soup.find("dl", attrs={"class":"indicator"})  # class가 두개 이상이면 list로 ex, attrs="class":["indicator","..."]
                                                         # class 뿐만 아니라 id도 함께 검색하고 싶을 떄는 dictionary니까 ex,{"class":"indicator","id":"dust"}
                                                         # 어떤 text까지 함께 검색하고 싶으면 find("dl", attrs = {"class":"indicator"}, text=["미세먼지","초미세먼지"])인 element를 찾게 된다
    pm10 = dust.find_all("dd")[0].get_text() # 미세먼지
    pm25 = dust.find_all("dd")[1].get_text() # 초미세먼지


    # 출력
    print(cast)
    print("현재 {} (최저 {} / 최고 {})".format(curr_temp, min_temp, max_temp))
    print("오전 {}/ 오후 {}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3) # li 태그 3개만
    for index, news in enumerate(news_list):
        title = news.find("a").get_text().strip()  # find는 첫번째 것만 찾으니까.
        link = url + news.find("a")["href"]
        print("{}. {}".format(index+1, title))
        print("  (링크 : {})".format(link))
    print()



if __name__ == "__main__":   # 해당 모듈이 임포트 된 경우가 아니라 인터프리터에서 직접 실행된 경우에만 if문을 실행
                             # 참조 (https://medium.com/@chullino/if-name-main-%EC%9D%80-%EC%99%9C-%ED%95%84%EC%9A%94%ED%95%A0%EA%B9%8C-bc48cba7f720)
    # 오늘의 날씨 정보 가져오기
    #scrape_weather()  # 인터프리터로 실행하면 scrape_weather가 뜨고, 임포트하면 안뜬다
    scrape_headline_news()