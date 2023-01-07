def solution(num_list, n):
    answer = [[[0 for i in range(n)] for j in range(len(num_list) // n)]]
    k = 0
    for i in range(len(num_list) // n):
        for j in range(n):
            answer[i][j] = num_list[k]
            k += 1
    print(answer)
    return answer

solution(num_list=[100, 95, 2, 4, 5, 6, 18, 33, 948], n = int(input()))

#
# def solution(num_list, n):
#     answer = []
#     for i in range(0, len(num_list), n):
#         answer.append(num_list[i:i+n])
#     return answer