import sys

t = int(sys.stdin.readline())
num_li = []
result = []

for _ in range(t):
    num_li.append(list(map(int, sys.stdin.readline().split())))

# print(num_li) [[1, 45000], [6, 10], [13, 17]]

# 유클리드 호제법: a,b (a>b) 가 있다고 할때, a와 b의 최대공약수는 b와 a%b(a를 b로 나눈 나머지)의 최대공약수 와 같다.
# ex) gcd(24,18) = gcd(18,6) = gcd(6,0) => b가 0이 되는 순간이 최대공약수이다.

for i in range(len(num_li)):
    m, n = num_li[i][0], num_li[i][1]
    while n != 0:
        m = m % n
        m, n = n, m

    max_div = m  # 최대공약수

    # 최소공배수 => lcm = gcd * (M//gcd) * (N//gcd) = M*N//gcd
    min_mul = num_li[i][0]*num_li[i][1]//m

    result.append(min_mul)

for i in range(len(result)):
    print(result[i])
