import sys

def hanoi(n, initial_pole, temp_pole, target_pole): ##(판 개수, 초기 장대, 예비 장대, 목표 장대)
    if n == 1:
        print(initial_pole, target_pole)
        return
    hanoi(n-1, initial_pole, target_pole, temp_pole) ## n-1개를 (초기 장대)에서 (예비 장대)로 옮긴다.
    print(initial_pole, target_pole) #초기 장대의 가장 밑에 있는 판을 (목표 장대)로 옮긴다.
    hanoi(n-1, temp_pole, initial_pole, target_pole) #n-1개를 (예비 장대)에서 (목표 장대)로 롦긴다.
    
n = int(sys.stdin.readline())
print(2**n-1)
hanoi(n, 1, 2, 3)

# n번째 원반을 한쪽 기둥으로 옮기는데 필요한 최소 횟수를 a(n)이라고 하면
# n+1 번째 원반을 옮기려면 {a(n+1)을 구하려면}
# n번째 까지의 원반을 한쪽 기둥으로 옮기고 (a(n)을 더하고)
# n+1 번째 원반을 비어 있는 기둥에 옮기고 (1을 더하고)
# n번째까지의 원반을 n+1번째 원반 위로 옮기면 된다. (a(n)을 다시 더하면)
# 따라서, a1=1이고 a(n+1) = 2a(n)+1이므로 수열 a(n)의 일반항을 구해보면 a(n)=2**n-1이 나온다.
# 일반항을 구하는 법은 다음과 같다
# 관계식 a(n+1)=2a(n)+1 -> a(n+1)+1 = 2{a(n)+1} -> b(n)=a(n)+1일 때, b(n+1)=2b(n)
# 따라서, b(n)은 b1=a1+1=2이고, 공비가 2인 등비수열이 된다.
# b(n)=a(n)+1=2**n -> a(n)=2**n-1이 나온다.