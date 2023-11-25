def solution(s):
    res = []; temp = []
    word = dict.fromkeys(s)
    for i, j in enumerate(s):
        if j not in temp:
            res.append(-1)
            temp.append(j)
            word[j] = i
        else:
            res.append(i - word[j])
            word[j] = i

    print(res)
solution(s = "banana")
solution(s = "foobar")