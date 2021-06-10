# bin(number): 전달받은 integer 혹은 long integer 자료형의 값을 이진수(binary) 문자열로 돌려준다.
# ex) bin(78) => '0b1001110'   '0b'는 2진수라는 뜻

def solution(n):
    print(bin(n))
    cnt_one = bin(n).count('1')
    for answer in range(n+1, 1000001):
        if bin(answer).count('1') == cnt_one:
            return answer


print(solution(78))
