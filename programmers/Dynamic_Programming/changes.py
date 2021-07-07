money = [1, 2, 5]
n = 5


def solution(n, money):
    answer = 0  # 방법 가지수

    # 부분 문제 (top-down || bottom-up)
    # memorization
    # Map: key = n, value = 거스름돈 가지수
    # n = 1 -> value = 1
    # n = 2 -> value = 2
    # n = 3 -> value = 2
    # n = 4 -> value = 3
    # n = 5 -> value = 4 -> (1,,,,1), (1,1,1,2), (1,2,2), (5)
    # n = 6 -> value = 5 -> (1......1), (2,2,2), (5,1) , (2,2,1,1), (1,1,1,1,2)

    rest = [1] + [0]*n
    # print("rest: ", rest)
    for m in money:  # 화폐 m
        for i in range(m, n+1):
            rest[i] += rest[i-m]  # i-m
            print("----------")
            print("m: ", m)
            print("i: ", i)
            print("rest: ", rest)

    return rest[n] % 10000000007


solution(n, money)
