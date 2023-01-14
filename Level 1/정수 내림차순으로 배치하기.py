def solution(n):
    n = list(str(n))
    n = ''.join(sorted(n, reverse= True))
    print(int(n))


solution(n = 118372)