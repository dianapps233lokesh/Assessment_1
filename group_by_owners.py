def group_by_owners(mp):
    ans={}
    # print(mp.items())
    for key,value in mp.items():
        if value in ans:
            ans[value].append(key)
        else:
            ans[value]=[key]
    return ans

print(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}))
# print(type(group_by_owners({'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'})))
