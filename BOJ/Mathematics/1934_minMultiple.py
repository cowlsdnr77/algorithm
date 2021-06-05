import sys


# pypy로 통과

def findMaxDiv(m, n):
    m_div_li = []
    n_div_li = []
    for i in range(1, m+1):  # m의 약수 구하기
        if m % i == 0:
            m_div_li.append(i)

    for i in range(1, n+1):  # n의 약수 구하기
        if n % i == 0:
            n_div_li.append(i)

    for i in range(0, len(m_div_li)):  # 최대공약수 구하기
        if m_div_li[i] in n_div_li:
            max_div = m_div_li[i]
    return max_div


t = int(sys.stdin.readline())
num_li = []
result = []
for _ in range(t):
    num_li.append(list(map(int, sys.stdin.readline().split())))

# print(num_li) [[1, 45000], [6, 10], [13, 17]]

for i in range(len(num_li)):
    max_div = findMaxDiv(num_li[i][0], num_li[i][1])
    min_mul = max_div*(num_li[i][0]//max_div)*(num_li[i][1]//max_div)
    result.append(min_mul)

for i in range(len(result)):
    print(result[i])
