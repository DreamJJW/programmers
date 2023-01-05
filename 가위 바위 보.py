from itertools import combinations
def solution(balls, share):
    answer = list(combinations(range(1, balls + 1), share))
    print(len(answer))
    return answer

solution(balls= 3, share= 2)