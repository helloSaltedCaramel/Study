# 대소문자 바꿔서 출력하기
# input: aBcDeFg
# output: AbCdEfG

r = ''
for i in input():
    if i.islower():
        r += i.upper()
    else :
        r += i.lower()
print(r)