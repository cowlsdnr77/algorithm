import sys

t = int(sys.stdin.readline())
result = []
for _ in range(t):
    ax, ay, ar, bx, by, br = map(int, sys.stdin.readline().split())

    # 두 점 사이의 거리 ((ax-bx)**2+(ay-by)**2)**0.5
    d = ((ax-bx)**2+(ay-by)**2)**0.5

    # 두 원이 일치할 때
    if ax == bx and ay == by and ar == br:
        result.append(-1)

    # 두 원이 외접할 때
    elif ar + br == d:
        result.append(1)

    # 두 원이 내접할 때
    elif ar == br + d or br == ar + d:
        result.append(1)

    # 두 원이 서로 떨어져 있고 만나지 않을 때 (바깥으로 떨어져 있을때와 원 안에서 떨어져 있을때)
    elif ar > br + d or br > ar + d or ar + br < d:
        result.append(0)

    else:
        result.append(2)


for i in result:
    print(i)
