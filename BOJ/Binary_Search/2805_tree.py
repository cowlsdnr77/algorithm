##함수 정의 안하면 pypy3에서는 통과, python3에서는 시간 초과
##함수 정의 하면 pypy3에서 통과, python3에서도 통과
import sys

def binarySearch(tree_arr, m):
    # tree_arr = [20, 15, 10, 17]
    ##벌목 높이를 움직여 필요 나무 길이를 채우는지 보는 것이다. [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    start_point = 1
    end_point = max(tree_arr)

    while start_point <= end_point: ##start_point가 end_point 보다 커지면 종료
        mid_point = (start_point+end_point)//2
        tree_sum = 0

        for i in tree_arr: ##입력된 나무 리스트의 값에 대하여
            if mid_point < i: ##mid_point가 입력된 나무 보다 작다면
                tree_sum += i-mid_point ##tree_sum에 잘린 나무 크기를 저장
        
        if tree_sum >= m: ##tree_sum이 가져가려고 하는 나무 길이 m 보다 크거나 같다면(즉, 더 많은 나무를 잘랐다면)
            start_point = mid_point+1 ## start_point를 현재 mid_point에 1을 더한 위치로 옮긴다.
        
        else: ##tree_sum이 가져가려고 하는 나무 길이 m 보다 작다면(즉, 잘린 나무가 부족하다면)
            end_point = mid_point-1 ##end_point를 현재 mid_point에 1을 뺀 위치로 옮긴다.

    print(end_point)

n,m = map(int, sys.stdin.readline().split())

tree_arr = list(map(int, sys.stdin.readline().split()))

binarySearch(tree_arr, m)