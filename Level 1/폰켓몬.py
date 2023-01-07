def solution(nums):
    pokemon = {}
    for i in nums:
        pokemon[i] = 1
    if len(nums) // 2 > len(pokemon):
        print(len(pokemon))
    else:
        print(len(nums) // 2)

    pick1 = nums[0]



solution(nums= [3,3,3,2,2,4])