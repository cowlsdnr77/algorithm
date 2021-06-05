import sys

n = int(sys.stdin.readline())  # n 은 홀수로 가정

num_li = []

for i in range(n):  # 숫자 입력
    num_li.append(int(sys.stdin.readline()))

# 산술평균
# 내장함수 sum을 쓰자!!
print(round(sum(num_li)/n))  # 소수점 첫번째에서 반올림

# 중앙값
sort_li = sorted(num_li)
print(sort_li[(len(sort_li)-1)//2])  # (맨처음 인덱스 + 맨끝 인덱스)//2

# 최빈값
# 딕셔너리 활용
# ****Counter 함수 찾아보기!!!!!!!*****
set_li = set(sort_li)  # 빈도수를 넣어주기 위해 중복된 값을 뺀 리스트 설정
num_dic = {}  # set_li의 값을 키로 설정한 딕셔너리

for i in (set_li):  # 딕셔너리 초기화
    num_dic[i] = 0

for i in (num_li):  # 딕셔너리의 value에 빈도수+1
    num_dic[i] += 1

count = 0  # 최빈값이 여러개 있을경우 두번째로 작은 값을 가져오기 위한 count
# set은 sort가 안되므로 다시 딕셔너리의 키값을 sort 해줌
sorted_keys_li = sorted(list(num_dic.keys()))
max_frequent = 0  # 최빈값

for i in sorted_keys_li:
    if num_dic[i] == max(num_dic.values()):  # 최대 빈도수와 i의 value값이 같다면 i는 최빈값
        count += 1
        max_frequent = i  # 최빈값을 저장
    if count == 2:  # 최빈값이 여러개일때 '두번째'로 작은 값 출력
        max_frequent = i
        break
print(max_frequent)

# 범위
if n == 1 or n == 2:  # n이 1이거나 2이면 범위가 없음
    print(0)
else:
    print(sort_li[-1]-sort_li[0])  # 최대값과 최소값의 차
