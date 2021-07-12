# 왼쪽 가장자리로 내려오는 경우/ 오른쪽 가장자리로 내려오는 경우 / 안쪽 나머지 경우
# 더하면서 값을 바꿔준다.

triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]


def solution(triangle):
    for i in range(1, len(triangle)):  # i는 현재 층
        for j in range(i+1):  # j는 현재 층 각 요소 위치
            if j == 0:  # 왼쪽 가장자리
                triangle[i][j] += triangle[i-1][j]  # 이전 층의 가장 왼쪽 요소 값을 더한다.
            elif j == i:  # 오른쪽 가장자리
                triangle[i][j] += triangle[i-1][i-1]  # 이전 층의 가장 오른쪽 요소 값을 더한다.
            else:  # 나머지
                # 이전 층의 요소 두개 중 큰 값을 더한다.
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


print(solution(triangle))
