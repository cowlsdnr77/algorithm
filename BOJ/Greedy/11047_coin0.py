import sys

# 그리디 알고리즘

N, K = map(int, sys.stdin.readline().split())

coin = []
count = 0

for _ in range(N):
    coin.append(int(sys.stdin.readline()))


for i in range(N-1, -1, -1):  # n-1~0까지
    if K // coin[i] != 0:
        count += K//coin[i]
        K -= coin[i] * (K//coin[i])
    else:
        continue
print(count)
