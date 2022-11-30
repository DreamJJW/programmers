def solution(A, B):
    answer = 0
    while True:
        if A == B:
            return answer
        A = A[-1] + A[:-1]
        answer += 1
        if answer == len(A):
            return -1

solution(A= input(), B= input())

