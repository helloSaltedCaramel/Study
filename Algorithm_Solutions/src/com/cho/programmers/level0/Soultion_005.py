# 문자열 붙여서 출력하기
# input: apple pen
# output: applepen

str1, str2 = input().strip().split(' ')

a = str1.replace(" ",'') 
b = str2.replace(" ",'')

print(a + b)