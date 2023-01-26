from collections import Counter
def solution(N, stages):
    a = []; answer = []
    players = len(stages)
    for i in range(1, N + 1):
        if stages.count(i) == 0:
            a.append((i, 0))
        else:
            a.append((i, stages.count(i) / players))
        players -= stages.count(i)
    
    a.sort(key=lambda x : -x[1])

    for i in a:
        answer.append(i[0])
    # print(answer)
    return answer


solution(N = 5, stages=[2,1,2,6,2,4,3,3])
# solution(N = 5, stages=[4,4,4,4,4])
# [1, 2, 2, 2, 3, 3, 4, 6]
# [1,2,3,4,6]


# 실패율 = 스테이지에 도달했으나 클리어못한 플레이어의 수  / 스테이지에 도달한 플레이어 수
# N = 전체 스테이지 개수, stages = 사용자가 현재 멈춰있는 스테이지의 번호
# 실패율이 높은 스테이지 번호를 내림차순으로 리턴


# 1차 70.4 / 100 점
# ZeroDivisionError: division by zero 런타임 오류가 나는 듯 했다.
# a.append((i, stages.count(i) / players))
# 유저 중 아무도 스테이지를 도달 못했을 경우 count = 0이 되어서 division by zero 에러가 떴다
# 해결 하였다

# 2차 100 / 100 점
# O(logn)으로 개선할 여지가 있다.

