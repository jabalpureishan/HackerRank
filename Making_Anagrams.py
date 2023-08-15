def anagram(s1,s2):
    d1,d2,count = {},{},0
    for i in s1:
        d1[i] = d1.get(i,0) + 1
    for i in s2:
        d2[i] = d2.get(i,0) + 1
    for i in d1:
        count += min(d1[i],d2.get(i,0))
    return len(s1) + len(s2) - 2*count