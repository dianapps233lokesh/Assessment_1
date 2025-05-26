def second_highest(nums):
    highest=max(nums)
    ans=float('-inf')
    for num in nums:
        if num < highest and num > ans:
            ans=num
    return ans

print(second_highest([9, 5, 1, 4, 8, 7, 2, 6, 3]))
            