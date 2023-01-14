def solution(n):
    answer = []; n = str(n)
    for i in n:
        answer.append(int(i))
    print(answer[::-1])



solution(n = 1000)