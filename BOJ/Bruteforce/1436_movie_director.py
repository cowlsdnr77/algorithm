import sys

N = int(sys.stdin.readline())


num = 666
count = 1  # 제목 카운트

if N == 1:  # 첫번째 제목을 찾는 경우
    print(num)
    exit()

while True:  # 두번째 제목 부터 탐색
    num = num + 1  # 666부터 1씩 더해가며 순차 탐색
    if '666' in str(num):  # 수에 '666'이 존재하는 경우
        count += 1  # 제목 카운트 + 1
    if count == N:  # 제목 카운트 가 입력받은 N과 동일한 경우
        print(num)
        break
