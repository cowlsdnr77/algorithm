n = 3
lost = [3]
reserve = [1]


def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+1)

    lost.sort()
    reserve.sort()

    for l in lost:
        students[l] -= 1

    print(students)

    for r in reserve:
        students[r] += 1

    print(students)

    for i in range(1, len(students)):
        if students[i] == 0:
            if i-1 >= 1 and students[i-1] > 1:
                students[i] += 1
                students[i-1] -= 1
            elif i+1 < len(students) and students[i+1] > 1:
                students[i] += 1
                students[i+1] -= 1
    print(students)

    for i in range(1, len(students)):
        if students[i] >= 1:
            answer += 1

    return answer


print(solution(n, lost, reserve))
