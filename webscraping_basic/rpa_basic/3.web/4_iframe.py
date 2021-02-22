# <html> 
#     <body>
#         <iframe id="1">
#             <html>
#                 <body>  
#                     <div.../>
#                 </body>
#             </html>
#         </iframe>
#     </body>
# </html>

#//*[@id="male"]

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')  # iframe id값
elem = browser.find_element_by_xpath('//*[@id="male"]') # 성공

elem.click()

browser.switch_to.default_content()  # 상위로 빠져나옴

# elem = browser.find_element_by_xpath('//*[@id="male"]') # 실패
# elem.click()


time.sleep(5)

browser.quit()
