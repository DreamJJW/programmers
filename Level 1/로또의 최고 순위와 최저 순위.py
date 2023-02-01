def solution(lottos, win_nums):
    a = []
    answer = []
    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    zero = lottos.count(0)
    for i in lottos:
        if i in win_nums:
            a.append(i)

    answer.append(score[len(a) + zero])
    answer.append(score[len(a)])
    print(answer)


solution(lottos=[44, 1, 0, 0, 31, 25], win_nums= [31, 10, 45, 1, 6, 19])
solution(lottos=[0, 0, 0, 0, 0, 0], win_nums=[38, 19, 20, 40, 15, 25])
solution(lottos=[45, 4, 35, 20, 3, 9], win_nums=[20, 9, 3, 45, 4, 35])


# 0의 숫자를 무조건 맞는걸로 세팅해버림
# 오류


