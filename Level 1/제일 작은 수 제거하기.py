def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 1:
        return [-1]
    print(arr)


solution(arr = [4,3,2,1])