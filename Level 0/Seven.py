def solution(array):
    answer = 0
    A = list(array)
    print(A)
    for _ in array:
        if '7' in array:
            answer += 1
    print(answer)
    return answer


solution(array=input())