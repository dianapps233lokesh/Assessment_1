def sort_ls(nums):
    n=len(nums)
    for i in range(n):
        for j in range(0,n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums


print(sort_ls([9, 5, 1, 4, 8, 7, 2, 6, 3]))