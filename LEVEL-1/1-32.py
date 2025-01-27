# Programmers 코딩 테스트 문제 (n의 배수)

# 문제 설명
# 정수 'num'과 'n'이 매개 변수로 주어질 때, num이 n의 배수이면 1을 return의 배수가 아니라면 0을 return하도록 solution() 함수를 완성하시오.

# 제한사항 
# 2 ≤ num ≤ 100
# 2 ≤ n ≤ 9

# 입출력 예
# num	n	result
# 98	2	  1
# 34	3	  0

# 입출력 예 설명
# 입출력 예1
# 98은 2의 배수이므로 1을 return 합니다.

# 입출력 예2
# 32는 3의 배수가 아니므로 0을 return합니다.

# Code
import sys 

# 함수 정의
def solution(num, n):
    answer = 0
    if num % n == 0:
        answer = 1
    # num이 n의 배수일 경우, answer = 1, 아닐 때 answer = 0
    return answer

# 메인 함수 (스크립트 실행 시 실행되는 부분)
if __name__ == "__main__":
    # test case
    print(solution(98, 2))  # 1
    print(solution(34, 3))  # 0