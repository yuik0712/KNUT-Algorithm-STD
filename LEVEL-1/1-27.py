# Programmers 코딩 테스트 문제 (문자열 섞기)

# 문제 설명
# 길이가 같은 두 문자열 'str1'과 'str2'가 주어질 때, 두 문자열의 각 문자가 앞에서부터 서로 번갈아가면서 한 번씩 등장하는 문자열을 만들어 'return' 하는 solution 함수를 완성해 주세요.


# 제한사항 
# 1 ≤ str1의 길이 = str2의 길이 ≤ 10
# str1과 str2는 알파벳 소문자로 이루어진 문자열입니다.

# 입출력 예
# str1	     str2	  result
# "aaaaa"	"bbbbb"	  "ababababab"

def solution(str1, str2):
    answer = ''
    for i in range(len(str1)):
        answer += str1[i] + str2[i]
    return answer

# 테스트
print(solution("aaaaa", "bbbbb"))  # "ababababab" 출력
print(solution("abc", "abc"))      # "aabbcc" 출력
