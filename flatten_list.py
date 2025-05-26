def flatten_ls(nums,ans):
    # ans=[]
    for num in nums:
        if isinstance(num,list):
            flatten_ls(num,ans)
        else:
            ans.append(num)
    return ans
    # print(ans)

print(flatten_ls([1,[2,[3,[4,[5,[6,[7]]]]]]],[]))