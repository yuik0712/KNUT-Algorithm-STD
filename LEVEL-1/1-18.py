# Programmers 코딩 테스트 문제 (a + b 출력하기)

# 문제 설명
# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

# 제한 사항
# -100,000 ≤ a, b ≤ 100,000

# 입출력 예
# Input: "4 5"
# Output:
    # a = 4
    # b = 5

# Point) Python 에서 'map' 함수 => 리스트나 반복 가능한 자료형의 요소를 일괄적으로 변환할 때 사용됨 / str => 문자열 / strip => 리스트

a, b = map(int, input().strip().split(' '))
if a>=-100000 and b<=100000 :
    print("a = " + str(a) ) # 첫 번째 값을 정수로 변환
    print("b = " + str(b) ) # 두 번째 값을 정수로 변환
else:
    print("다시 입력해주세요.")