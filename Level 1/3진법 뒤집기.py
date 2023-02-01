def solution(n):
    answer = 0
    a = ''
    while n >= 1:
        n, b = divmod(n, 3)
        a += str(b)
    print(int(a, 3))


solution(n = 45)

# int함수는 n진수를 10진수로 알아서 변환해준다.
# divmod를 사용하여 n진수 변환