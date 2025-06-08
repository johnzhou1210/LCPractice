def goldilocks_approved(nums):
    # edge case 
    if len(nums) <= 2:
        return -1

    # we need to account for duplicates
    lowest = min(nums)
    highest = max(nums)

    # [1,1,2,1,4]
    # min = 1
    # max = 4
    # 

    for num in nums:
        if num != lowest and num != highest:
            return num
    return -1

nums = [3, 2, 1, 4]
print(goldilocks_approved(nums))

nums = [1, 2]
print(goldilocks_approved(nums))

nums = [2, 1, 3]
print(goldilocks_approved(nums))
