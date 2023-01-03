from collections import Counter
def solution(array):
    a = []
    cnt = Counter(array)
    mode = cnt.most_common()
    mx = mode[0][1]

    for num in mode:
        if num[1] == mx:
            a.append(num[0])
    if len(a) > 1:
        print(-1)
    else:
        print(mode[0][0])

solution(array= list(map(int, input().split())))


# [2, 2, 5, 5, 6]