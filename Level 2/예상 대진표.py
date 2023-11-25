def solution(n,a,b):
    if a > b:
        a, b = b, a

    answer = 1
    while True:
        if abs(a-b) == 1 and a % 2 != 0:
            break

        if a % 2 != 0:
            a += 1
        a //= 2

        if b % 2 != 0:
            b += 1
        b //= 2

        answer += 1

    print(answer)
    return answer

solution(n=8, a=7, b=6)
