def solution(data, col, row_begin, row_end):
    temp = []
    data = sorted(data, key=lambda x: (x[col-1], -x[0]))
    for i in range(row_begin-1, row_end):
        s = 0
        for j in range(len(data[0])):
            s += (data[i][j] % (i+1))
        temp.append(s)

    answer = 0
    for i in temp:
        answer ^= i

    return answer

solution(data=[[2,2,6],[1,5,10],[4,2,9],[3,8,3]], col=2, row_begin=2, row_end=3)