import sys

# '조합' 으로 해결 -> mCn = m!/((m-n)!*n!)


def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)


t = int(sys.stdin.readline())

result = []

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result.append(factorial(m)//(factorial(m-n)*factorial(n)))

for i in result:
    print(i)
