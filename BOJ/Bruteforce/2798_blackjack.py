import sys

n, m = map(int, sys.stdin.readline().split())

num_li = list(map(int, sys.stdin.readline().split()))

max_val = 0

for i in range(0, n):  # num_li[0]~num_li[n-1]
    for j in range(i+1, n):  # num_li[i+1]~num_li[n-1]
        for k in range(j+1, n):  # num_li[j+1]~num_li[n-1]
            if num_li[i]+num_li[j]+num_li[k] == m:  # 정확히 일치할때
                max_val = m
                break
            elif num_li[i]+num_li[j]+num_li[k] < m:  # m에 가장 근접할때
                # 현재 max_val과 num_li[i]+num_li[j]+num_li[k] 중 큰 값을 max_val로 설정
                max_val = max(max_val, num_li[i]+num_li[j]+num_li[k])

print(max_val)
