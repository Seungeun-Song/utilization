# 정규식 

'''주민등록번호
901201-111111 (o)
abcdef-111111 (x)
901201-11111111 (x)

이메일 주소
nadocoding@gmail.com (o)
nudocoging@gmail@gmail.com (x)

IP 주소
192.168.0.1 (o)
1000.2000.3000.4000 (x)'''

import re
# abcd, book, desk
# ca?e
# care, cafe, case, cave ...
# caae, cabe, cace, cade, ...


#p = pattern
p = re.compile("ca.e")     
# . (ca.e): 하나의 문자를 의미 > care, cafe, case (o)  | caffe(x)
# ^ (^de): 문자열의 시작 > dest, destination (o) | fade#p (x)
# $ (se$) : 문자열의 끝 > case, base(o) | face(x)

'''m = p.match("case")  # patter(P)와 매치가 되는지
print(m.group())  # 매치되지 않으면 에러가 발생'''


'''n = p.match("caffe")
# print(n.group())
if n:
    print(n.group())
else:
    print('매칭되지 않음')'''

def print_match(m):
    if m:
        print("m.group() : ", m.group())  # 일치하는 문자열 반환
        print("m.string : ", m.string) # 입력받은 문자열을 그대로 반환   # string은 함수가 아니라 변수기 때문에 괄호x
        print("m.start() : ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() : ", m.end())  # 일치하는 문자열의 끝 index
        print("m.span() : ", m.span())   # 일치하는 문자열의 시작과 끝 index를 함께
    else:
        print('매칭되지 않음')
    
'''m = p.match("good care")
print_match(m)

m = p.match("careless") # match : 주어진 문자열의 처음부터 일치하는지 확인
print_match(m) '''


'''m = p.search("good care") # search : 주어진 문자열 중에 일치하는 게 있는지 확인
print_match(m)

m = p.search("careless") 
print_match(m)'''


'''lst = p.findall("careless")  # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)
lst = p.findall("good care cafe")  
print(lst)'''


1. p = re.compile("원하는 형태의 정규식")
2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인 
3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는 게 있는지 확인
4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 *리스트* 형태로 반환

원하는 형태 : 정규식
 . (ca.e): 하나의 문자를 의미 > care, cafe, case (o)  | caffe(x)
 ^ (^de): 문자열의 시작 > dest, destination (o) | fade#p (x)
 $ (se$) : 문자열의 끝 > case, base(o) | face(x)