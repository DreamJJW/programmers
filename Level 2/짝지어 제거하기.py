def solution(s):
    temp = []
    for i in s:
        if not temp:
            temp.append(i)
        else:
            if i == temp[-1]:
                temp.pop()
            else:
                temp.append(i)

    if temp: return 0
    else: return 1


solution(s = "baabaa")
# solution(s = "cdcd")