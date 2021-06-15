import collections

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    dic = {}

    for i in participant:
        if i in dic.keys():
            dic[i] += 1
        else:
            dic[i] = 1
    # {'mislav': 2, 'stanko': 1, 'ana': 1}

    for i in completion:
        if i in dic.keys():
            dic[i] -= 1
    # {'mislav': 1, 'stanko': 0, 'ana': 0}

    for key, value in dic.items():
        if value == 1:
            return key
    # mislav


print(solution(participant, completion))


# Counter 라이브러리 활용한 풀이
def solution2(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


# hash 활용한 풀이
def solution3(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer

# sort 후 비교하는 풀이


def solution4(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]
