def solution(s):
    answer = ''
    temp = list(map(int, s.split()))
    temp.sort()
    answer += str(temp[0]) + ' ' + str(temp[-1])
    return answer

solution(s="-1 -2 -3 -4")