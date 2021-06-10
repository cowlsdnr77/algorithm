clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]


# 해쉬: 키-밸류

# 종류(key) -> [i][1]: 얼굴, 상의, 하의, 겉옷
# 이름(value) -> [i][0]: "이름"

# Counter 모듈 사용해보기


def solution(clothes):
    answer = 1
    col_dict = {}  # key(종류) - value(개수)

    for i in range(len(clothes)):
        if col_dict.get(clothes[i][1]):
            col_dict[clothes[i][1]] += 1
        else:
            col_dict[clothes[i][1]] = 1

    for i in col_dict:
        answer *= (col_dict[i]+1)  # 종류를 사용안하는 경우 +1

    answer -= 1  # 종류 전체 사용안하는 경우 -1

    return answer


print(solution(clothes))

# from collections import Counter
# def solution(clothes):
#     temp = []
#     for name, kind in clothes:  # 이름과 종류 따로 뽑음
#         temp.append(kind)
#         # print(temp)
#     # print(temp)
#     counter = Counter(temp)
#     # print(counter['headgear'])
#     # 의상 종류의 개수들 구함
#     all_possible = 1  # 모든 경우의수 초기값(곱이므로 1)
#     for key in counter:
#         # print(counter[key])
#         all_possible *= (counter[key] + 1)  # 각 종류의 +1을 곱하며 더한다
#     return all_possible-1  # 아무것도 안입을 경우 빼기
# print(solution([["yellowhat", "headgear"], [
#       "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]))
