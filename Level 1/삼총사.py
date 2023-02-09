from itertools import combinations
def solution(number):
    cnt = 0
    lst = combinations(number, 3)
    for i in lst:
        if sum(i) == 0:
            cnt += 1
    print(cnt)
    return cnt

solution(number=[-2,3,0,2,-5])
solution(number=[-3, -2, -1, 0, 1, 2, 3])
solution(number=[-1,1,-1,1])