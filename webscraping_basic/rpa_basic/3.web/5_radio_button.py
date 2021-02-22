from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')  # iframe id값
elem = browser.find_element_by_xpath('//*[@id="male"]') 

# 체크가 안되어 있으면 선택하기
if elem.is_selected() == False: # 라디오버튼이 선택되어 있지 않으면
    print('선택 안되어 있으므로 선택하기')
    elem.click()
else: # 라디오버튼이 선택되어 있으면
    print('선택 되어 있으므로 아무것도 안함')

time.sleep(5)
#browser.quit()

if elem.is_selected() == False: # 라디오버튼이 선택되어 있지 않으면
    print('선택 안되어 있으므로 선택하기')
    elem.click()
else: # 라디오버튼이 선택되어 있으면
    print('선택 되어 있으므로 아무것도 안함')