# 홀짝 구분하기

# str1	     str2	      result
# "aaaaa"	"bbbbb"	    "ababababab"
          
def solution(str1, str2):
    answer = ''
    for i in range(0, len(str1)):
        answer = answer + str1[i] + str2[i]
    return answer 