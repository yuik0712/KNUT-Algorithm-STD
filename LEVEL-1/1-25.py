# Programmers 코딩 테스트 문제 (홀짝 구분하기)

# 문제 설명
# 자연수 n이 입력으로 주어졌을 때 만약 n이 짝수이면 "n is even"을, 홀수이면 "n is odd"를 출력하는 코드를 작성해 보세요.

# 제한사항 
# 1 ≤ n ≤ 1,000

# 입출력 예
# 입력1: "100"
# 출력1: "100 is even"

# 입력2: "1"
# 출력2: "1 is odd"

a = int(input())

if a % 2 == 0:
    print(f"{a} is even")


else:
    print(f"{a} is odd")

# Point) 모듈로 연산자(%)를 사용한 짝수/홀수 판별과 조건문을 통한 결과 출력