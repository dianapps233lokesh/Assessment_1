def flatten_ls(nums):
    ans=[]
    for num in nums:
        if isinstance(num,list):
            ans.append(flatten_ls(num))
        else:
            ans.append(num)
    # return ans
    print(ans)

print(flatten_ls([1,[2,[3,[4,[5,[6,[7]]]]]]]))