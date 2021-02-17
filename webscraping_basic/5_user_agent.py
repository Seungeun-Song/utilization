# requests로 받아올 수 없을 때.. user agent를 사용/ 접속하는 브라우저에 따라 user agent 주소가 달라져
# headers의 user-agent를 명명함으로써 url에 접속할 때 명명한 user-agent로 들어가게 되는 것
import requests

url = "http://nadocoding.tistory.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36"}
res = requests.get(url, headers=headers)
res.raise_for_status()
with open("nadocoding.html","w", encoding="utf8") as f:
    f.write(res.text)

