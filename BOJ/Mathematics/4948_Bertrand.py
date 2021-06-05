import sys


def prime_list(n):
    num_list = [True] * n  # num_list[0], num_list[1] 은 소수가 아니라 쓸일 없음

    for i in range(2, int(n**0.5) + 1):  # 2부터 n의 제곱근까지의 모든 수를 확인
        if num_list[i] == True:  # 소수일때
            for j in range(2*i, n, i):  # 소수를 제외한 소수의 배수들을 false로 바꿈
                num_list[j] = False
    # 2부터 n 까지 중 소수인 요소들만 리스트로 반환
    return [i for i in range(2, n) if num_list[i] == True]


result = []  # 출력할 값의 리스트

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    if n == 1:
        result.append(1)
    else:
        res_list = prime_list(2*n)  # 2부터 2n 사이에 있는 소수 들의 리스트
        # res_list 요소 중 n 보다 큰 요소들만 저장한 리스트의 길이(= n부터 2n 사이의 소수 개수)를 저장
        result.append(len([i for i in res_list if i > n]))

for i in range(len(result)):
    print(result[i])
