# Programmers 코딩 테스트 문제 (문자열 반복해서 출력하기)

# 문제 설명
# 문자열 str과 정수 n이 주어질 때, str이 n번 반복된 문자열을 만들어 출력하는 코드를 작성해 보세요.

# 제한 사항
# 1 ≤ str의 길이 ≤ 10
# 1 ≤ n ≤ 5

# 입출력 예
# Input: "yuik 5"
# Output: "yuikyuikyuikyuikyuik"

# Point) str => 문자열 / strip => 리스트 / input => 사용자가 입력한 값을 받아서 str, n으로 저장, 그 이후 str을 n번 반복하여 출력

str, n = input().strip().split(' ')
n = int(n)

print(str*n)