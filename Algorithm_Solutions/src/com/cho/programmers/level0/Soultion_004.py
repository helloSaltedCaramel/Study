# 덧셈식 출력하기
# input: 4 5
# output: 4 + 5 = 9

a, b = map(int, input().strip().split(' '))

if 1 <=a <=100 and 1<=b<=100: 
    print(f'{a} + {b} = {a+b}') 