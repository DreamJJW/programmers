def two_bit(n, x):
    a = format(x, 'b')
    return a

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        arr1[i] = two_bit(n, arr1[i])
        arr2[i] = two_bit(n, arr2[i])
        a = (str(int(arr1[i]) + int(arr2[i])))
        if len(a) < n:
            a = '0' * (n - len(a)) + a
        answer.append(a)

    for i in range(len(answer)):
        answer[i] = str(answer[i]).replace('1', '#')
        answer[i] = str(answer[i]).replace('2', '#')
        answer[i] = str(answer[i]).replace('0', ' ')

    # print(answer)
    return answer


solution(n = 6, arr1= [46,33,33,22,31,50], arr2=[27,56,19,14,14,10])

# 101110
#  11011
# 111111



