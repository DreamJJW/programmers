def solution(k, score):
    hall = []; min_hall = []
    cnt = 0
    for i in score:
        hall.append(i)
        cnt += 1
        if cnt > k:
            hall.remove(min(hall))
        min_hall.append(min(hall))

    print(min_hall)



solution(k=4, score=[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000])


# pop과 remove를 적절히 사용