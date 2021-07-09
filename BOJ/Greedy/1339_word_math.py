import sys

# PS
# 각 알파벳이 몇번째 자리에 쓰이는지 파악
n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().rstrip() for i in range(n)]
alpha_list = {}
num_list = []

for word in word_list:
    for i in range(len(word)):
        if word[i] in alpha_list.keys():
            alpha_list[word[i]] += pow(10, len(word)-1-i)  # 자릿수를 더해준다.
        else:
            alpha_list[word[i]] = pow(10, len(word)-1-i)

for value in alpha_list.values():
    num_list.append(value)

num_list.sort(reverse=True)

answer, number = 0, 9
for num in num_list:
    answer += num*number
    number -= 1

print(answer)
