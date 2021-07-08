
# 제한 사항
# 논문의 수는 1편 이상 1000편 이하
# 논문별 인용 횟수는 0회 이상 10,000회 이하

# 발표한 논문 n편 중, h 번 이상 인용된 논문이 h편 이상이고
# 나머지 논문이 h번 이하 인용되었다면
# h의 최댓값이 이 과학자의 H-index이다.


# 문제를 이해하기가 너무 어려웠다.
# 풀이 참고함


citations = [3, 0, 6, 1, 5]


def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    h = len(citations)

    while True:
        count = 0
        for c in citations:
            if c >= h:  # 현재 요소가 h 이상이면
                count += 1
            if count >= h:
                return h
        h -= 1


# h-index에 대한 설명: https://www.ibric.org/myboard/read.php?Board=news&id=270333
def solution2(citations):
    citations.sort(reverse=True)
    for i, n in enumerate(citations):
        if n <= i:
            return i
    return len(citations)


# sort로 정렬해서 가장 큰값부터 작은값으로 정렬한후, enumerate로 (index, value)형태로 묶는다.
# 그리고 최댓값(start = 1)부터 각 value에 대해 최솟값 value의 값을 min으로 추출하고,
# 이 추출된 값은 enumerate가 끝나는 citations 리스트의 크기에 해당하는 갯수가 나온다.
# 이들을 map으로 묶으면, 한 value의 입장에서 보는 최솟값 value의 집합이 나온다.
# 즉 h값들의 집합이나온다. h값중 최대값을 max로 뽑아서 출력하면 된다.
# "이해 못함...."
def solution3(citations):
    citations.sort(reverse=True)  # [6,5,3,1,0]
    answer = max(map(min, enumerate(citations, start=1)))
    return answer


print(solution3(citations))
