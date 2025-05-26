def missing_number(nums):
    n=nums[-1]
    natural_sum=n*(n+1)/2
    mis_num=natural_sum-sum(nums)
    return int(mis_num)

print(missing_number([1,2,3,5]))