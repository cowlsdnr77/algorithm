import sys

# 바이토닉 수열은 3가지로 나눌수 있음
# 기준수 k를 기준으로
# 1) {+~k} -> k 까지 증가하는 수열
# 2) {+~k~-} -> k까지 증가했다가 k이후부터 감소하는 수열
# 3) {k~-} -> k부터 감소하는 수열
# 바이토닉 수열이 가장 길게 위해서는 1)과 3)을 더한 2)를 구하면 됨

n = int(sys.stdin.readline())

sequence = list(map(int, sys.stdin.readline().split()))
foward_result = [1 for i in range(n)]  # 앞에서부터 증가하는 수열 최대 길이 저장 리스트
backward_result = [1 for i in range(n)]  # 뒤에서부터 증가하는 수열 최대 길이 저장 리스트

# foward_result와 backward_result의 각 인덱스 값(길이)의 합 저장 리스트
final_result = [1 for i in range(n)]


# 앞에서부터 증가하는 수열 최대 길이 저장
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            foward_result[i] = max(foward_result[i], foward_result[j]+1)

# print(foward_result)

# 뒤에서부터 증가하는 수열 최대 길이 저장
for i in range(n-2, -1, -1):
    for j in range(n-1, i, -1):
        if sequence[j] < sequence[i]:
            backward_result[i] = max(backward_result[i], backward_result[j]+1)

# print(backward_result)

# foward_result와 backward_result를 더함
for i in range(len(final_result)):
    # 자기 자신이 중복되므로 -1
    final_result[i] = foward_result[i] + backward_result[i] - 1

# print(final_result)
print(max(final_result))
