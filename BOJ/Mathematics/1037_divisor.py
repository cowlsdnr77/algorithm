import sys

number = int(sys.stdin.readline())

divisor_li = list(map(int, sys.stdin.readline().split()))

# 진짜 약수는 1 과 N을 제외한 N의 약수

# 15 = 1,3,5,15

# 32 = 1, 2, 4 ,8, 16 32

# divisor_li의 가장 큰 값과 가장 작은 값을 곱한게 N

print(max(divisor_li) * min(divisor_li))
