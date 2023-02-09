def solution(numbers):
    answer = 0
    for i in range(10):
        if i not in numbers:
            answer += i
    print(answer)

solution(numbers = [1,2,3,4,6,7,8,0])