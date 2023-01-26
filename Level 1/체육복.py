def solution(n, lost, reserve):
    student = []
    answer = 0
    for i in range(1, n+1):
        student.append(i)
    # 여벌이 없고 자신의 체육복만 있는 학생 제거
    for i in student:
        if i not in lost and i not in reserve:
            student.remove(i)

    for i in reserve:
        if i - 1 in lost:
            student.remove(i - 1)
            student.remove(i)

    print(n - len(student))



solution(n = 3, lost = [3], reserve=[1])
# student = [1,2,3,4,5]