import sys
# 가장 긴 증가하는 부분 수열
# 입력 예시
# 6
# 10 20 10 30 20 50

size = int(sys.stdin.readline())  # 수열 A의 크기
a_list = []  # 수열 A의 값들을 저장할 리스트

# memo = { 1 : {a: 10, count: 1 }, 2 : {a: 20, count: 2}, ... }
memo = {}

# 리스트 a_list에 수열 값들 저장
# [10, 20, 10, 30, 20, 50]
a_list = list(map(int, sys.stdin.readline().split()))


## memo[1] = {'a': 10, 'count': 1}

length = 0  # 길이

for num in range(len(a_list)):
    temp_count = 0

    if memo == {}:  # memo가 비어있다면 a_list 맨 처음 값을 추가
        memo[1] = {'a': a_list[0], 'count': 1}
        length += 1
        print("memo:", memo)
    else:
        for i in range(1, len(memo)+1):
            if a_list[num] > memo[i]['a']:  # a_list의 값과 memo에 들어있는 값들의 'a' 와 비교
                if temp_count < memo[i]['count']:
                    temp_count = memo[i]['count']

        # a_list의 값과 count 값을 memo[num+1] 에 추가
        memo[num+1] = {'a': a_list[num], 'count': temp_count+1}
        print("memo:", memo)

        if length < temp_count+1:
            length = temp_count+1

# print("memo: ", memo)
print(length)
