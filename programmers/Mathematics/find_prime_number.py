from itertools import permutations
from math import sqrt

numbers = "17"


def prime_check(number):
    if number == 0 or number == 1:
        return False
    else:
        for i in range(2, int(sqrt(number)+1)):
            if number % i == 0:
                return False
    return True


def solution(numbers):
    answer = 0
    num_list = list(numbers)
    check_list = []
    for i in range(1, len(num_list)+1):
        for j in permutations(num_list, i):  # permutation으로 가져온 j은 튜플형태
            # 튜플을 ''.join(j)를 통해 string으로 바꾼 후 int()로 정수로 변환
            check_list.append(int(''.join(j)))
    check_list = set(check_list)
    print(check_list)

    for i in check_list:  # 시퀀스들은 for 문 돌릴 수 있음
        if prime_check(i):
            answer += 1

    return answer


# 순열로 모든 경우의 수 찾는다
# 모든 경우의 수에 대해 소수를 찾는다.
print(solution(numbers))
