from itertools import combinations
def solution(numbers):
    answer = []
    a = list(combinations(numbers, 2))
    for i in a:
        answer.append(sum(i))
    answer = list(set(answer))
    print(answer)

solution(numbers = [2,1,3,4,1])