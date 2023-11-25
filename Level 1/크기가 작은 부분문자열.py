def solution(t, p):
    temp = []
    len_p = len(p) # 3
    for i in range(len(t) - len_p + 1):
        temp.append(t[i:len_p + i])

    cnt = 0
    for i in temp:
        if int(i) <= int(p):
            cnt += 1

    print(cnt)

solution(t = "3141592", p = "271")
solution(t = "500220839878", p = "7")
solution(t = "10203", p = "15")

#5 0 0 2 2 0 8 3 9 8 7 8