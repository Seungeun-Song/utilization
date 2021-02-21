import requests
from bs4 import BeautifulSoup
import re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")
    return soup

def print_news(idx, title, link):
    print(idx+1, title)
    print("   (링크 : %s)" %(link))

# 오늘의 날씨
def scarpe_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&oquery=%EC%84%9C%EC%9A%B8%EB%82%A0%EC%94%A8&tqi=hv4aTsp0JXVsslE0lFhssssss%2FZ-290408"
    soup = create_soup(url)
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    temp = soup.find("p", attrs={"class":"info_temperature"}).get_text().replace("도씨","")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    morning_rainfall = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rainfall = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()
    dust = soup.find("dl", attrs={"class":"indicator"}).find_all("dd")

    print(cast)
    print("현재 %s (최저 %s / 최고 %s)" %(temp, min_temp, max_temp))
    print("오전 %s / 오후 %s" %(morning_rainfall, afternoon_rainfall))
    print()
    print("미세먼지 %s" %(dust[0].get_text()))
    print("초미세먼지 %s" %(dust[1].get_text()))
    print()
# [헤드라인 뉴스]
def scrape_headline_news():
    print("[헤드라인 뉴스]")
    url = "https://news.naver.com"
    soup = create_soup(url)
    newslist = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=3)
    for idx, news in enumerate(newslist):
        title = news.find("a").get_text().strip()
        link = url + news.find("a")["href"]
        print_news(idx, title, link)
    print()


#[IT 뉴스]
def scrape_it_news():
    print("[IT 뉴스]")
    url = "https://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)
    newslist = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=3)
    for idx, news in enumerate(newslist):
        a_idx = 0
        img = news.find("img")
        if img:
            a_idx = 1
        title = news.find_all("a")[a_idx].get_text().strip()
        link = news.find_all("a")[a_idx]["href"]
        print_news(idx, title, link)
    print()

#[오늘의 영어 회화]
def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)
    sentences = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()    
    print("(한글 지문)")
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()


if __name__ == "__main__":   
    scarpe_weather()
    scrape_headline_news()
    scrape_it_news()
    scrape_english()
