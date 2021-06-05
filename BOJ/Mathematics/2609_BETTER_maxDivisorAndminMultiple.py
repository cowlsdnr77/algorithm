import sys

M, N = map(int, sys.stdin.readline().split())

m, n = M, N

# 유클리드 호제법: a,b (a>b) 가 있다고 할때, a와 b의 최대공약수는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 와 같다.
# ex) gcd(24,18) = gcd(18,6) = gcd(6,0) => b가 0이 되는 순간이 최대공약수이다.

while n != 0:
    m = m % n
    m, n = n, m

print(m)  # 최대공약수

print(M*N//m)  # 최소공배수 => lcm = gcd * (M//gcd) * (N//gcd) = M*N//gcd
