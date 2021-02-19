from selenium import webdriver
import time

browser = webdriver.Chrome()

# 1. 네이버 이동
browser.get("http://naver.com")

# 2. 로그인 버튼 클릭
elem = browser.find_element_by_class_name("link_login")
elem.click()

# 3. id, pw입력
browser.find_element_by_id("id").send_keys("naver_id") # id는 입력만 하는 거니까 변수로 받을 필요 없어서 .send_keys붙여줘
browser.find_element_by_id("pw").send_keys("password")


# 4. 로그인 버튼 클릭
browser.find_element_by_id("log.login").click()

time.sleep(3)

# 5. id를 새로 입력
#browser.find_element_by_id("id").send_keys("my_id")
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

# 6. html정보 출력
print(browser.page_source)

# 7. 브라우저 종료
browser.quit()