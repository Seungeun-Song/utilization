from selenium import webdriver

#browser = webdriver.Chrome("C:/Users/SONG/utilization/chromedriver.exe")
browser = webdriver.Chrome()

browser.get("http://naver.net")

elem = browser.find_element_by_link_text('카페')
elem

elem.get_attribute("href")
elem.get_attribute("class")
#>>'nav'
browser.back()
browser.forward()
browser.refresh()
browser.back()
elem = browser.find_elements_by_id("query")
elem
elem.send_keys('나도코딩')
#enter치기
from selenium.webdriver.common.keys import Keys
elem.send_keys(Keys.ENTER)
