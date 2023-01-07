def solution(chicken):
    bonus = 0; coupon = 0
    while chicken > 0:
        bonus += chicken // 10
        print(bonus)
        coupon += chicken % 10
        print(coupon)
        chicken = chicken // 10
    bonus += coupon // 10
    print(bonus)

solution(chicken=int(input()))
