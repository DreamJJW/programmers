from itertools import combinations
def isPrime(n):
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(nums):
    cnt = 0
    a = list(combinations(nums, 3))
    for i in a:
        if isPrime(sum(i)) == True:
            cnt += 1
    print(cnt)

solution(nums= [1,2,3,4])
