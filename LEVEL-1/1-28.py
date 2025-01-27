# Programmers 코딩 테스트 문제 (문자 리스트를 문자열로 변환하기)

# 문제 설명
# 문자들이 담겨 있는 배열'arr'가 주어질 때, 'arr'의 원소들을 순서대로 이어 붙인 문자열을 return하는 solution 함수를 작성하여라

# 제한사항 
# 1 ≤ arr의 길이 ≤ 200
# arr의 원소는 전부 알파벳 소문자로 이루어진 길이가 1인 문자열입니다.

# 입출력 예
# arr	         	  result
# ["a", "b', "c"]	  "abc"

def solution(arr):
    answer = ''
    for i in arr:
        answer += i
    return answer

print(solution(["a", "b", "c"]))