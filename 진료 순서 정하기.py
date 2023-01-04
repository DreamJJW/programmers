def solution(emergency):
    temp = emergency
    answer = []
    emergency = sorted(emergency, reverse=True)
    dic = {string: i + 1 for i, string in enumerate(emergency)}
    print(dic)
    for i in range(len(emergency)):
        answer.append(dic.get(temp[i]))
    print(answer)

# solution(emergency=[30, 10, 23, 6, 100])

