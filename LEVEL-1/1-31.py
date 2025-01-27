# Programmers 코딩 테스트 문제 (두 수의 연산값 비교하기)

# 문제 설명
# 연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 
# 예) 12 ⊕ 3 = 123, 3 ⊕ 12 = 312
# 양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.
# 단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.

# 제한사항 
# 1 ≤ a, b < 10,000

# 입출력 예
# a	b	result
# 2	91	364
# 91	2	912

# 입출력 예 설명
# 입출력 예1
# a ⊕ b = 291 이고, 2 * a * b = 364 입니다. 둘 중 더 큰 값은 364 이므로 364를 return 합니다.

# 입출력 예2
# a ⊕ b = 912 이고, 2 * a * b = 364 입니다. 둘 중 더 큰 값은 912 이므로 912를 return 합니다.

import sys

def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)

# 테스트 케이스 추가
if __name__ == '__main__':
    # 입출력 예에 따른 테스트
    test_cases = [
        (2, 91), # 입출력 예 1
        (91, 2), # 입출력 예 2
        (10, 20), # 추가 테스트
        (5, 5) # 추가 테스트
    ]

for a, b in test_cases:
    result = solution(a, b)
    print(f"input: {a}, b = {b} -> output: {result}")