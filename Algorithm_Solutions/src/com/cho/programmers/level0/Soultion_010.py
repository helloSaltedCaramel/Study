# 홀짝 구분하기

# my_string	k	result
#"string"	3	"stringstringstring"
#"love"	10	"lovelovelovelovelovelovelovelovelovelove"
          
def solution(my_string, k):
    answer = ''
    answer = my_string*int(k)
    return answer