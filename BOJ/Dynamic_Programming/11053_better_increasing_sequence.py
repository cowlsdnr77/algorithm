import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
# [10, 20, 10, 30, 20, 50]
result = [1 for i in range(N)]

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            result[i] = max(result[i], result[j]+1)

# print(result)
print(max(result))
