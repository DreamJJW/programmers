def solution(a, b, n):
    cnt = 0
    if n < a:
        return 0
    while n >= a:
        x, y = divmod(n, a)
        cnt += (x * b)
        n = x*b + y

    print(cnt)

solution(a = 3, b = 2, n = 20)