# 못풀고 구글링함

import sys
import math

T = int(sys.stdin.readline())

results = []

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    distance = y - x

    # distance의 제곱근 값의 올림 ex)distance=18, factor = 5
    factor = math.ceil(math.sqrt(distance))

    # 앞뒤의 제곱수를 구함 (거리가 제곱수)
    flag1 = (factor - 1) ** 2
    flag2 = factor ** 2

    if distance >= (flag1 + flag2)/2:  # 앞뒤 제곱수의 중간 값보다 크거나 같다면
        res = factor * 2 - 1
    else:  # 앞뒤 제곱수의 중간 값보다 작다면
        res = factor * 2 - 2

    results.append(res)

for result in results:
    print(result)


# distance    route   count   move_distance(구하려는 값)
# 1            11       1           1
# 2            11       2           1
# 3           111       3           2
# 4*          121       3           2
# 5          1211       4           2
# 6          1221       4           2
# 7         12211       5           3
# 8         12221       5           3
# 9*        12321       5           3
# 10       123211       6           3
# 11       123221       6           3
# 12       123321       6           3
# 13      1233211       7           4
# 14      1233221       7           4
# 15      1233321       7           4
# 16*     1234321       7           4
# 17     12343211       8           4
# 18     12343221       8           4
# 19     12343321       8           4
# 20     12344321       8           4
# 21    123443211       9           5
# 22    123443221       9           5
# 23    123443321       9           5
# 24    123444321       9           5
# 25*   123454321       9           5
