def solution(num):
    cnt = 0
    if num == 1:
        return 0
    while num > 0:
        if num % 2 == 0:
            num //= 2
        elif num % 2 != 0:
            num = (num * 3) + 1
        cnt += 1
        if num == 1:
            break
    if cnt > 500:
        return -1
    return cnt


solution(num = 16)