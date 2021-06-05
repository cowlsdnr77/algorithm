import sys
n = int(sys.stdin.readline())

input_list = []  # 수열을 이루는 정수를 저장하는 리스트
stack = []  # 숫자를 push&pull 하는 스택
result_list = []  # 연산 순서대로 숫자를 저장하는 리스트
operations = ""  # 연산 정보를 저장하는 String

for i in range(n):
    input_list.append(int(sys.stdin.readline()))

num = 1  # 1~n까지 숫자를 위한 초기값 => 리스트로 만들지 않고 num 값에 +1을 해주면서 값을 증가시킴
cnt = 0  # input_list의 인덱스 값을 위한 변수


while True:
    # 수열의 숫자 값과 일치할때(stack[-1]과 비교)까지 스택에 push
    # 수열의 숫자 값과 일치하면(stack[-1] == input_list[i]) pull해서 result_list에 저장

    if result_list == input_list:  # 성공 종료 조건
        break

    if len(stack) == 0:  # 스택에 아무것도 들어있지않다면
        stack.append(num)  # num을 스택에 push
        num += 1
        # print(stack)
        operations += "+"
        continue

    if input_list[cnt] != stack[-1]:  # 스택 맨 위 값과 수열의 cnt번째 값이 같지 않을때
        if num > n:  # 실패 종료 조건// num이 입력받은 n 보다 클때
            print("NO")
            break
        # num <= n 이라면 num을 스택에 push
        stack.append(num)
        num += 1
        # print(stack)
        operations += "+"
    else:  # 스택 맨 위 값과 수열의 cnt번째 값이 같을때
        result_list.append(stack.pop())
        cnt += 1  # 수열의 요소를 가르키고 있는 cnt를 증가시킴
        # print(stack)
        operations += "-"


if len(stack) == 0:  # 연산 정보를 출력
    for i in operations:
        print(i)
