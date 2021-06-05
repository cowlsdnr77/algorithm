import sys


def factorial(num):
    # num = 0 일때 고려안해주면 recursion Error 발생 (무한루프)
    if num == 0:  # 0!은 1임 => 1! = 1 x (1-1)! = 1 x 0! = 1
        return 1
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)


n, k = map(int, sys.stdin.readline().split())

result = factorial(n)//(factorial(k)*factorial(n-k))
print(result)
