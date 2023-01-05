def solution(numbers, k):
    # 2 < numbers < 100
    numbers = numbers * 100
    j = 0
    # print(numbers)
    for i in range(k):
        a = numbers[j]
        j += 2
    print(a)
    return a



solution(numbers=[1, 2, 3, 4, 5 ,6], k = 5)




