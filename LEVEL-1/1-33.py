# Programmers 코딩 테스트 문제 (공배수)

# 문제 설명
# 정수 number와 n, m이 주어질 때, number가 n의 배수이면서 m의 배수이면 1을 아니라면 0을 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 10 ≤ number ≤ 100
# 2 ≤ n, m < 10

# 입출력 예
# number	n	m	result
# 60	    2	3	  1
# 55	    10	5	  0

# 입출력 예 설명
# 입출력 예1
# 60은 2의 배수 이면서 3의 배수이기 때문에 1을 return 합니다,

# 입출력 예2
# 55는 5의 배수이지만 10의 배수가 아니기 때문에 0을 return 합니다.

import sys 

# 함수 정의
def solution(number, n, m):
    return 1 if number % n == 0 and number % m == 0 else 0 # ex) solution(60, 2, 3) -> 1


# test case
print(solution(60, 2, 3))  # 1
print(solution(55, 10, 5))  # 0

sys.exit(0)  # exit code 0 for successful execution.

# sys.exit(1)  # exit code 1 for unsuccessful execution.

# 코드 분석) solution 함수는 number를 n, m의 배수로 나눈 나머지가 0 이면 1, 0 이면 0을 return합니다.