import sys

N = int(sys.stdin.readline())

word_list = []
for i in range(N):
    word_list.append(sys.stdin.readline().rstrip())

cnt = 0

for word in word_list:
    tmp = []
    for i in range(len(word)):
        if i < len(word)-1:
            if word[i] != word[i+1]:
                if word[i+1] not in tmp:
                    tmp.append(word[i])
                else:  # 탈출 조건
                    cnt -= 1
                    break
        else:  # 맨 마지막 글자 처리
            tmp.append(word[i])
    cnt += 1


print(cnt)
