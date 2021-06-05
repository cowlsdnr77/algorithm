import sys


def binary_search(target, have_array):
    start = 0  # 맨 처음의 위치
    end = len(have_array)-1  # 가장 마지막의 위치
    mid = (start+end)//2  # 중간 지점의 위치
    while start <= end:
        if have_array[mid] == target:  # 리스트의 중간 지점 위치 값과 같은 경우
            return 1
        elif have_array[mid] < target:  # 리스트의 중간 지점 위치 값보다 큰 경우
            start = mid+1
        else:  # 리스트의 중간 지점 위치 값보다 작은 경우
            end = mid-1

        mid = (start+end)//2  # start 또는 end 가 바뀌었기 때문에 중간값 다시 설정

        if start > end:  # 탈출조건: start가 end보다 크면 => 리스트에 target 값이 없음
            return 0


N = int(sys.stdin.readline())  # 상근이가 가지고 있는 숫자 카드 개수
have_numbers = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())  # 판별이 필요한 숫자 카드 개수
compare_numbers = list(map(int, sys.stdin.readline().split()))

result = []

have_numbers.sort()

for m in compare_numbers:
    result.append((binary_search(m, have_numbers)))

print(*result)  # 언팩킹.. print(result) => [1,0,0,1,1,0,0,1]
# print(*result) => 1 0 0 1 1 0 0 1
