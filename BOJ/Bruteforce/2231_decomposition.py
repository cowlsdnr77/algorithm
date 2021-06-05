import sys

n = int(sys.stdin.readline())

# 분해합은 자기 자신 + 각 자리 숫자

min_comp = 1000000  # 가장 작은 생성자 구하기 위해 설정

for i in range(n-1, 0, -1):  # n의 생성자는 n보다 작으므로 n-1 ~ 1까지의 범위를 탐색
    sum = i  # sum은 분해합
    for j in range(len(str(i))):
        sum += int(str(i)[j])  # sum에 각 자리 숫자를 더해줌
    if sum == n:  # 분해합이 n과 같다면 i는 생성자
        min_comp = i  # i는 감소하므로 해당 조건을 만족할때마다 가장 작은 생성자로 갱신됨

if min_comp != 1000000:  # 생성자가 있으면 min_comp 초기값에 변화가 있음
    print(min_comp)
else:  # 생성자가 아예 없으면 min_comp은 초기값 그대로임
    print(0)


# 다른 풀이
# num = input()


# for i in range(0,int(num)):
#     sum=0
#     for j in range(len(str(i))):
#         sum += int(str(i)[j])
#     if sum + i == int(num):
#         print(i)
#         break
# else:
#     print(0)
