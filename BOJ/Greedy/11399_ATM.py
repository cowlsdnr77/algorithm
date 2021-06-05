import sys

# P1 = 3, P2 = 1, P3 = 4, P4 = 3, P5 = 2

# P: [2, 5, 1, 4, 3]
# 시간: 1, 2, 3, 3, 4 => 최소값

# 가장 시간 적게 걸리는 사람부터 정렬

n = int(sys.stdin.readline())
result = 0  # 시간의 합
tmp = 0  # 각 사람마다 걸리는 시간

time_li = list(map(int, sys.stdin.readline().split()))

time_li.sort()

for i in range(n):
    tmp += time_li[i]  # i 번째 사람까지 걸리는 시간을 더함
    result += tmp  # 각 사람이 필요한 시간을 더해줌

print(result)
