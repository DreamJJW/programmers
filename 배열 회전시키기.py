def solution(numbers, direction):
    if direction == "left":
        numbers = numbers[1:] + list(numbers[:1])
    elif direction == "right":
        numbers = list(numbers[-1:]) + numbers[:-1]
    print(numbers)




solution(numbers=[4, 455, 6, 4, -1, 45, 6], direction= "right")


# [4, 455, 6, 4, -1, 45, 6, 4, 455, 6, 4, -1, 45, 6]
# [455, 6, 4, -1, 45, 6, 4]