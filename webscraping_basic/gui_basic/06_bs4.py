# pip install beautifulsoup4  스크래핑하기 위해 사용되는 패키지
# pip install lxml 구문을 분석하는 파써

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")  # 가져오는 html 문서를 lxml파써를 통해서 beautifulsoup 객체로 만든 것
#print(soup.title)
#print(soup.title.get_text())
#print(soup.a)   # soup 객체에서 첫번째로 발견되는 a태그에 대한 element를 뿌려주는
#print(soup.a.attrs)  # attrs = attributes 속성 / 딕셔너리형태로 출력
#print(soup.a["href"]) # a element의 href 속성 '값'정보를 얻을 수 있다
''' ^ 이건 페이지에 대한 이해도가 높을 때, 무슨 속성이 어디쯤 어떻게 들어가 있는지 알 때 사용'''

#print(soup.find('a', attrs={"class" : "Nbtn_upload"})) # a 태그에 해당하는 첫번째 element의 속성이 class=Nbtn_upload인 것을 출력
#print(soup.find(attrs={"class" : "Nbtn_upload"})) # Nbtn_upload이 유일할 때. a이든 아니든.

#print(soup.find("li", attrs={"class":"rank01"}))
#rank1 = soup.find("li", attrs={"class":"rank01"})
#print(rank1.a.get_text())
#print(rank1.next_sibling)  # 왜 두번 적어야 출력되는가? 페이지마다 개행(줄바꿈)정보가 있어서 그럴 수도 있다
# rank2 =rank1.next_sibling.next_sibling
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())
#print(rank1.parent)


# rank2 = rank1.find_next_sibling("li") # li정보만 찾는다. 그럼 개행정보는 안나오겠지
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling('li')
# print(rank2.a.get_text())

#print(rank1.find_next_siblings("li"))

webtoon = soup.find("a", text="고수-2부 135화") # a에서 text가 "고수" 인 것을 가져온다
print(webtoon)