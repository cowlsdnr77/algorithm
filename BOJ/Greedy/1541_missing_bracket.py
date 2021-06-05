import sys

expression = sys.stdin.readline().rstrip()

# -을 기준으로 나누자

sub_list = expression.split("-")

# print(sub_list)  # ['55', '50+40']

sum = 0

for i in range(len(sub_list)):
    tmp = 0

    add_list = sub_list[i].split("+")  # +를 기준으로 다시 나눔
    for j in range(len(add_list)):
        tmp += int(add_list[j])

    if i == 0:  # sub 리스트의 맨 앞이면
        sum += tmp
    else:
        sum -= tmp

print(sum)


# 내장함수 sum을 활용한 풀이
# equation=input().split("-")

# parts_list=[]

# for i in equation:
#     part=sum(list(map(int,i.split("+"))))
#     parts_list.append(part)

# print(parts_list[0]-sum(parts_list[1:]))
