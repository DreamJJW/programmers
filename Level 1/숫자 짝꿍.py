def solution(X, Y):
    x = {x: 0 for x in X}
    y = {y: 0 for y in Y}
    temp = []
    for i in X:
        x[i] += 1
    for i in Y:
        y[i] += 1

    for a, b, in x.items():
        if a in y.keys():
            while x[a] > 0 and y[a] > 0:
                temp.append(a)
                x[a] = x[a] - 1
                y[a] = y[a] - 1
            
    if len(temp) == 0:
        return -1

    if sum(map(int, temp)) == 0:
        return 0

    temp = sorted(temp, reverse=True)
    temp = "".join(temp)
    return temp


# solution(X = "12321", Y = "42531")
# solution(X = "100", Y = "203045")
solution(X = "5525", Y = "1255")
# solution(X = "100", Y = "2345")