from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) # url로 이동

# 가는 날 선택 클릭
browser.find_element_by_link_text("가는날 선택").click()

# 이번 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[0].click() # [0] ->이번달   # element's' - 27에 관련된 모든 element를 가져오는.. 그리고 그 중 첫번째[0]
# browser.find_elements_by_link_text("28")[0].click() # [0] ->이번달

# 다음 달 27일, 28일 선택
# browser.find_elements_by_link_text("27")[1].click() # [1] -> 다음 달
# browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 이번 달 27, 다음 달 28일 선택
browser.find_elements_by_link_text("27")[0].click() # [1] -> 다음 달
browser.find_elements_by_link_text("28")[1].click() # [1] -> 다음 달

# 제주도 선택
browser.find_element_by_xpath('//*[@id="recommendationList"]/ul/li[1]').click()

# 항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

# 검색 결과 기다리기
try :
    # webdriverwait를 통해서, 최대 10초동안 대기/until(언제까지)? EC(어떤 조건에 의해서 기다리는데) By.XPATH라는 조건으로 xpath값에 해당하는 element가 나올때까지 기다리는
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[2]/div/div[4]/ul/li[1]'))) 
    # 성공했을 때 동작 수행.
    print(elem.text)# 첫번째 결과 출력
    # 성공 안하면 그냥 끝내는
finally:
    browser.quit()

# 첫번째 결과 출력
# elem = browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[4]/ul/li[1]')
# print(elem.text)