def solution(i, j, k):
    s = ''; cnt = 0
    for i in range(i, j + 1):
        s += str(i)
    for i in s:
        if i == str(k):
            cnt += 1
    return cnt

solution(i = int(input()), j = int(input()), k = int(input()))

# 15, 25, 35, 45, 50
# 3,4,5,6,7...