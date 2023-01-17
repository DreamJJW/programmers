def solution(n, m):
    A = []; B = []
    for i in range(1, n+1):
        if n % i == 0:
            A.append(i)
    for i in range(1, m+1):
        if m % i == 0:
            B.append(i)
    print(A)
    print(B)

solution(n = 3, m = 12)

#유클리드 호제법 사용

