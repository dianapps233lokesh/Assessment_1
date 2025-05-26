def highest_freq(s):
    mp={}
    for chr in s:
        if chr in mp:
            mp[chr]+=1
        else:
            mp[chr]=1
    max_freq=0
    
    for chr in s:
        if mp[chr]>max_freq:
            ans=chr
            max_freq=mp[chr]
    return ans

print(highest_freq('hello'))
        
    