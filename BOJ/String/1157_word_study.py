str = input().upper()

alpa_arr = []
for i in range(1, 27):
    alpa_arr.append(0)

# ord는 아스키 코드 숫자값을 반환
# chr은 문자를 반환

for i in str:
    alpa_arr[ord(i)-65] += 1

max = 0
tmp = 0
for i in range(len(alpa_arr)):
    if max < alpa_arr[i]:
        max = alpa_arr[i]
        tmp = i

alpa_arr.sort(reverse=True)
if alpa_arr[0] == alpa_arr[1]:
    print("?")
else:
    print(chr(tmp+65))
