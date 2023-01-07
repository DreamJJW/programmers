def solution(n):
    answer = []
    # for i in range(2, n + 1):
    #     if n % i == 0:
    #         answer.append(i)
    #         n = n // i
    k = 2
    while n >= 2:
        if n % k == 0:
            answer.append(k)
            n = n // k
        elif n % k != 0:
            k += 1
    answer = dict.fromkeys(answer)
    print(list(answer))
    return list(answer)

solution(n = int(input()))