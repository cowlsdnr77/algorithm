m, n = map(int, input().split())

list = [True]*(n+1)

x = int(n**0.5)

for i in range(2, x+1):
    if list[i] == True:
        for j in range(i*2, n+1, i):
            list[j] = False

for i in range(2, len(list)):
    if i >= m:
        if list[i] == True:
            print(i)
