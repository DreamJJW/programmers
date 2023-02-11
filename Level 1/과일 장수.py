def solution(k, m, score):
    answer = 0; box = 0
    score.sort()
    for i in range(len(score), 0, -m):
        temp = score[i-m:i]
        answer += len(temp) * min(temp)
        box += 1
        print(temp)
        if box == (len(score) // m):
            break
    print(answer)

# solution(k = 3, m = 4, score= [1,2,3,1,2,3,1])
# solution(k = 4, m = 3, score= [4,1,2,2,4,4,4,4,1,2,4,2])
# solution(k = 4, m = 4, score = [4, 4, 3, 3, 3, 2, 2, 2, 1])

# solution(k = 9, m = 2, score= [7, 7, 6, 5, 2] )
solution(k = 7, m = 2, score= [7, 7, 5, 3, 3, 3, 1])

# 사과 1점 = 최하품, k점 = 최상품
# 한 상자에 사과가 m개
# 상자에 담긴 사과 중 가장 낮은 점수가 p점일 경우, 사과 상자의 가격은 p * m
# 얻을 수 있는 최대 이익, 상자 단위로 판매, 남는 사과는 버림

# 테스트 케이스 16번만 오류가 뜬다.
# 95.8 / 100점
# 해결 실패
