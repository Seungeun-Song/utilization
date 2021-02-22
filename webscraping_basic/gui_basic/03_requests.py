# 웹 페이지(HTML) 읽어오기

import requests
#res = requests.get("http://naver.com")
#res = requests.get("http://nadocoding.tistory.com")
#print("응답코드 :", res.status_code) # 200이면 정상/ 403이면 접근불가

'''if res.status_code == requests.codes.ok:
    print('정상입니다')
else:
    print('문제가 생겼습니다. [에러코드 ', res.status_code, "]")'''



'''res.raise_for_status()   # 정상이면 진행, 문제가 생겼을 때는 오류를 내고 프로그램을 끝내
print("웹 스크랩핑을 시작합니다")'''



'''res = requests.get("http://naver.com")
res.raise_for_status()
print(len(res.text))'''


res = requests.get("http://google.com")
res.raise_for_status()
print(len(res.text))
print(res.text)

with open("mygoogle.html","w",encoding="utf8") as f:
    f.write(res.text)