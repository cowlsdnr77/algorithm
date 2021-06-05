import sys

m, n = map(int, sys.stdin.readline().split())

m_div_li = []  # m의 약수 리스트
n_div_li = []  # n의 약수 리스트

max_div = 0
min_mul = 0

for i in range(1, m+1):  # m의 약수 구하기
    if m % i == 0:
        m_div_li.append(i)

for i in range(1, n+1):  # n의 약수 구하기
    if n % i == 0:
        n_div_li.append(i)

for i in range(0, len(m_div_li)):  # 최대공약수 구하기
    if m_div_li[i] in n_div_li:
        max_div = m_div_li[i]

min_mul = max_div*(m//max_div)*(n//max_div)  # 최소공배수 구하기

print(max_div)
print(min_mul)
