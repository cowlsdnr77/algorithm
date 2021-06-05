import sys

n = int(sys.stdin.readline())

tri_li = []

for i in range(n):
    tri_li.append(list(map(int, sys.stdin.readline().split())))
    #[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:  # 왼쪽 가장자리
            tri_li[i][j] = tri_li[i-1][j] + tri_li[i][j]
        elif j == i:  # 오른쪽 가장자리
            tri_li[i][j] = tri_li[i-1][j-1] + tri_li[i][j]
        else:  # 나머지 경우
            tri_li[i][j] = max(tri_li[i-1][j-1], tri_li[i-1][j]) + tri_li[i][j]

print(max(tri_li[n-1]))
