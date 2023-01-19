def solution(arr1, arr2):
    for i in range(len(arr1)):
        for j in range(len(arr2)):
            arr1[i][j] += arr2[i][j]
    print(arr1)

solution(arr1 = [[1,2,4], [2,3,4]], arr2 = [[3,4,4], [5,6,4]])
# solution(arr1 = [[1], [2]], arr2 = [[4],[6]])