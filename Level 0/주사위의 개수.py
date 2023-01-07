def solution(box, n):
    answer = 0
    a = box[0] // n; b = box[1] // n; c = box[2] // n
    print(a * b * c)
    return answer

solution(box= [10, 8, 6], n = int(input()))