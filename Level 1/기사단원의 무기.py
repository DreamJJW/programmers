def solution(number, limit, power):
    temp = [];
    cnt = 0
    for i in range(1, number + 1):
        for j in range(1, int(i**0.5) + 1):
            if j * j == i:
                cnt += 1
            elif i % j == 0:
                cnt += 2
        temp.append(cnt)
        cnt = 0

    for i in range(len(temp)):
        if temp[i] > limit:
            temp[i] = power

    print(sum(temp))

solution(number=10, limit=3, power=2)

# 시간 초과
# def solution(number, limit, power):
#     temp = []; cnt = 0
#     for i in range(1, number+1):
#         for j in range(1, i + 1):
#             if i % j == 0:
#                 cnt += 1
#         temp.append(cnt)
#         cnt = 0
#
#     for i in range(len(temp)):
#         if temp[i] > limit:
#             temp[i] = power
#
#     print(sum(temp))

# 제곱근의 수 만큼 돌려서 O(루트N)만큼의 시간 단축