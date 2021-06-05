import sys

n = int(sys.stdin.readline())

result = []
tile = ["00", "1"]

count = 0
length = 0
sequence = ""


def dp(n, length, sequence):
    # 수열 길이가 n과 같고 수열이 수열 저장 리스트에 없을때
    if length == n:
        if sequence not in result:
            result.append(sequence)
        return

    elif length > n:
        return

    for i in range(len(tile)):
        if i == 0:
            length += 2
        else:
            length += 1
        sequence += tile[i]
        dp(n, length, sequence)


dp(n, 0, sequence)
print(result)
