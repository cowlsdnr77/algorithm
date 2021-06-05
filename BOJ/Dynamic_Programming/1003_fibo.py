import sys

# fibo(3) 을 찾아와라!

# 1. memo[3]이 있는지 본다.
# 2. 없으니까 fibo(2) + fibo(1) 을 구해야 한다.
# 3. 그러면 memo[2] 와 memo[1] 이 있는지 찾아본다.
# 3-1. memo[2]가 없으니까 fibo(1) + fibo(0) 을 구해야 한다.
# 3-2. 그러면 memo[1] 과 memo[0]이 있는지 찾아본다.
# 3-3. 있으니까 그 값을 가져온 뒤 fibo(2) 을 만든다.
# 3-4. memo[2] 에 fibo(2) 를 기록한다.
# 4. memo[2]와 memo[1]을 더해서 fibo(3) 을 만든다.
# 5. memo[3] 에 fibo(3) 을 기록한다.

# memo[0]과 memo[1]이 호출되는 횟수를 구하라


def fibo(n, fibo_memo, zero_one_list):
    # 구현해보세요!
    if n in fibo_memo:
        return fibo_memo[n]

    nth_fibo = fibo(n-1, fibo_memo, zero_one_list) + \
        fibo(n-2, fibo_memo, zero_one_list)
    fibo_memo[n] = nth_fibo
    zero_one_list[n] = [zero_one_list[n-1][0] + zero_one_list[n-2]
                        [0], zero_one_list[n-1][1] + zero_one_list[n-2][1]]

    return nth_fibo


t = int(sys.stdin.readline())  # 테스트 케이스 개수 T 입력
n = []  # N 값을 저장할 리스트

for i in range(t):
    n.append(int(sys.stdin.readline()))  # 리스트 n에 N 값 저장

for i in n:
    memo = {  # memo 라는 변수에 Fibo(0)과 Fibo(1) 값을 저장
        0: 0,
        1: 1
    }

    zero_one_list = {  # zero_one_list 라는 변수에 Fibo(0)과 Fibo(1) 호출 횟수를 리스트로 저장
        0: [1, 0],
        1: [0, 1]
    }

    # print("fibo : ", fibo(i, memo, zero_one_list))
    fibo(i, memo, zero_one_list)
    print(*zero_one_list[i])
