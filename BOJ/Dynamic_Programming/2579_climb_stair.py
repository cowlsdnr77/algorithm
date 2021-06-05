import sys

n = int(sys.stdin.readline())
stairs = []
dp = []  # "n번째 계단까지 계산했을때 가장 큰 경우 값"들을 저장하는 리스트 (메모이제이션)


for _ in range(n):
    stairs.append(int(sys.stdin.readline()))
    #[10, 20, 15, 25, 10, 20]

dp.append(stairs[0])  # 1번째 계단까지의 점수 최대값
dp.append(max(stairs[0]+stairs[1], stairs[1]))  # 2번째 계단까지의 점수 최대값
dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))  # 3번째 계단까지의 점수 최대값

# 문제에서 필요한 조건 중 3번을 만족시키기 위해 맨 마지막 계단(= END)이 밟혀있다고 가정해보자.
for i in range(3, n):
    # 그렇다면 그 전의 계단은 "END - 1" 계단이거나, 맨 마지막 "END - 2" 계단 일 것이다.
    # i) 전 계단이 "END - 1" 계단이라면, "END - 1" 계단의 전 계단은 "END - 2"가 되면 안되므로 "END - 3" 이다.
    # ii) 전 계단이 "END - 2" 계단이라면, "END - 1" 계단의 전 계단은 고려하지 않아도 된다.
    # 그러므로 i)와 ii) 중 더 큰 값이 dp[END]값이다.
    dp.append(max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i]))

print(dp.pop())
