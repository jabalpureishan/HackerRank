def isvalid(s):
    d = {}
    for i in s:
        d[i] = d.get(i,0) + 1
    dd = {}
    for i in d.values():
        dd[i] = dd.get(i,0) + 1
    Max = max(dd.values())
    Min = float("inf")
    for i in dd:
        if dd[i]==Max:
            Min = min(Min,i)
    #print(d)
    remove = 0
    for i in d:
        if d[i]!=Min:
            if d[i]==1:
                remove+=1
            else:
                remove += d[i]-Min
    if remove>1:
        return "NO"
    return "YES"
    
    

print(isvalid("abc"))
print(isvalid("abcc"))
print(isvalid("aabcc"))
print(isvalid("abccc"))
print(isvalid("aabbc"))
print(isvalid("aaacc"))
print(isvalid("aabbcd"))
print(isvalid("aabbccddeefghi"))
