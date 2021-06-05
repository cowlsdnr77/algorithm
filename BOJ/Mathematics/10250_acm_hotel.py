def hotel(h, w, m):
    cnt = 0
    output = ""
    for i in range(1, w+1):
        for j in range(1, h+1):
            cnt += 1
            if cnt == m:
                if i < 10:
                    output = str(j) + "0" + str(i)
                else:
                    output = str(j) + str(i)
                print(output)


t = int(input())
for i in range(t):
    h, w, m = map(int, input().split())
    hotel(h, w, m)
