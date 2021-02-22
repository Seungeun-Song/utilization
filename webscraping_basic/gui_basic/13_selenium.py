# selenium - 웹 페이지 자동화 , 동적 페이지 일 때 쉬움
# web driver 설치 - chrome drive.exe

from selenium import webdriver

browser = webdriver.Chrome()  # "C:/Users/SONG/utilization/chromedriver.exe"
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem

elem.click()

browser.back()
browser.forward()
browser.refresh()

elem = browser.find_element_by_id("query")
elem

from selenium.webdriver.common.keys import Keys  # keys.enter을 위해. 즉 엔터를 치기 위해서. 검색버튼을 find할 거면 필요X
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)

elem = browser.find_elements_by_tag_name("a")
elem

for e in elem:
    e.get_attribute("href")  #href 전부 찾기
    # 또 엔터 누르면 출력

browser.get("http://daum.net")

elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem.send_keys(Keys.ENTER)
browser.back()

elem = browser.find_element_by_name("q")
elem.send_keys("나도코딩")
elem = browser.find_element_by_xpath('//*[@id="daumSearch"]/fieldset/div/div/button[2]') # xpath 이용
elem
elem.click()

browser.close()  # 현재 창만 창 닫기
browser.quit()   # 잔체 브라우저 닫기
exit() # 파이썬 종료