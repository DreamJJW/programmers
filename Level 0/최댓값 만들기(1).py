def solution(numbers):
    answer = 0
    numbers.sort()
    return numbers[-1] * numbers[-2]

solution(numbers= [0, 31, 24, 10, 1, 9])