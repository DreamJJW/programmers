from itertools import combinations
def solution(d, budget):
    answer = 0
    d.sort()
    for i in range(len(d)):
        if d[i] <= budget:
            answer += 1
            budget -= d[i]
    print(answer)

# def solution(d, budget):
#     d.sort()
#     while budget < sum(d):
#         d.pop()
#     return len(d)


solution(d = [1,3,2,5,4], budget=9)
# 1 2 3 4 5
# 1 3 5 = 9
