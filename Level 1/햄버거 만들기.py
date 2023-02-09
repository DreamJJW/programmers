def solution(ingredient):
    hamburger = []
    cnt = 0
    for i in ingredient:
        hamburger.append(i)
        if hamburger[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for j in range(4):
                hamburger.pop()

    return cnt

solution(ingredient=[2, 1, 1, 2, 3, 1, 2, 3, 1])

# 1 빵, 2 야채, 3 고기
# 빵 2개와 고기 1개


