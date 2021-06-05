import sys

memo = {
    1: 1,
    2: 1,
    3: 1,
    4: 2,
    5: 2
}


def dp(n):
    if n in memo.keys():
        return memo[n]

    memo[n] = dp(n-5) + dp(n-1)
    return memo[n]


T = int(sys.stdin.readline())

result = []

for _ in range(T):
    n = int(sys.stdin.readline())
    result.append(dp(n))

for i in result:
    print(i)
