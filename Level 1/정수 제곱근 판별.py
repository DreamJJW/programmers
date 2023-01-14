import math
def solution(n):
    answer = 0
    if math.sqrt(n).is_integer():
        print(int(math.sqrt(n) + 1) ** 2)
    else:
        print(-1)
    return answer

solution(n = 3)