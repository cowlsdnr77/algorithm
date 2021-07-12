# dfs로 풀어야할듯
# dfs는 스택으로 풀자
# 더하거나 빼진 합이 다음 노드
numbers = [1, 2, 3]
target = 4


# 반복적 DFS로 푸는 코드
def solution(numbers, target):
    # result_list는 0부터 시작한다. 그리고 [0,0-a,0+a,0-a-b,0-a+b,0+a-b,0+a+b, ...] 이런식으로 저장됨
    result_list = [0]

    for i in range(len(numbers)):
        temp_list = []
        # result_list에는 0부터 numbers의 각 원소들을 빼고 더한 값들이 있다.
        for j in range(len(result_list)):
            # 현재 result_list에 다음 숫자를 더하거나 뺀다
            temp_list.append(result_list[j] - numbers[i])
            temp_list.append(result_list[j] + numbers[i])
        # temp_list 자체가 결국 현재 단계까지의 result_list 이므로
        result_list = temp_list
        print(result_list)
    return result_list.count(target)


# 재귀적 DFS로 푸는 코드
answer = 0


def dfs(numbers, target, length, i):
    global answer
    print("i: ", i)
    print("numbers: ", numbers)
    if i == len(numbers):
        if (sum(numbers)) == target:
            answer += 1
            return
    else:
        # numbers의 i번째 값을 양수, 음수로 나눠서 재귀
        dfs(numbers, target, length, i+1)
        numbers[i] *= -1  # [-1,1,1,1,1]와 같은 방식으로 분기해서 재귀되는것
        dfs(numbers, target, length, i+1)


def recursive_solution(numbers, target):
    global answer
    length = len(numbers)
    dfs(numbers, target, length, 0)
    return answer


print(recursive_solution(numbers, target))
