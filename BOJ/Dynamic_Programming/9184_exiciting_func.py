import sys

# dp의 메모이제이션 사용해서 top-down 방식 써야할듯
# key-point : 딕셔너리의 키 값으로 튜플도 가능하다
# key-point : 파이썬 format 함수 사용

dp_memo = {
    # (a,b,c) = value (= dp_w(a,b,c) 값)
}


def dp_w(a, b, c):
    if (a, b, c) in dp_memo.keys():  # 메모 딕셔너리에 (a,b,c)라는 튜플 형태의 키가 있다면
        return dp_memo[(a, b, c)]  # 해당 키의 value 값 (즉, dp_w(a,b,c)의 값)을 반환

    if a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a > 20 or b > 20 or c > 20:  # 20보다 크면 그냥 메모에 저장된 dp_w(20,20,20) 값을 반환
        dp_memo[(20, 20, 20)] = dp_w(20, 20, 20)
        return dp_memo[(20, 20, 20)]

    elif a < b and b < c:
        dp_memo[(a, b, c)] = dp_w(a, b, c-1) + \
            dp_w(a, b-1, c-1) - dp_w(a, b-1, c)
        return dp_memo[(a, b, c)]
    else:
        dp_memo[(a, b, c)] = dp_w(a-1, b, c) + dp_w(a-1, b-1, c) + \
            dp_w(a-1, b, c-1) - dp_w(a-1, b-1, c-1)
        return dp_memo[(a, b, c)]


result = []

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1:
        break
    result.append('w({}, {}, {}) = {}'.format(a, b, c, dp_w(a, b, c)))

for i in result:
    print(i)
