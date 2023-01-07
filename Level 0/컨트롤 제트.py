def solution(s):
    answer = 0
    a = []
    s = list(s.split())
    for num in s:
        if num != 'Z':
            a.append(int(num))
        else:
            a.pop(-1)
    print(sum(a))

    return answer

solution(s = "-1 -2 -3 Z")