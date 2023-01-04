def solution(rsp):
    answer = ''
    rsp = list(rsp)
    win = {'2': '0', '0': '5', '5': '2'}
    for i in rsp:
        answer += win.get(i)
    return answer
solution(rsp='2')