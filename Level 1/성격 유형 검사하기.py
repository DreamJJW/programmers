def solution(survey, choices):
    a = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    answer = ''
    for i, j in zip(survey, choices):
        if j > 4:
            a[i[1]] += j - 4
        elif j < 4:
            a[i[0]] += 4 - j
    print(a)

    li = list(a.items())

    for i in range(0, 8, 2):
        if li[i][1] < li[i + 1][1]:
            answer += li[i + 1][0]
        else:
            answer += li[i][0]

    return answer


solution(survey= ["AN", "CF", "MJ", "RT", "NA"], choices= [5, 3, 2, 7, 5])