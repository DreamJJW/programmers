def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    # 2월은 29일 (윤년)
    day = 0
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(a - 1):
        day += months[i]
    day += b
    days = days * 52
    print(days[day - 1])


solution(a = 5, b = 24)
