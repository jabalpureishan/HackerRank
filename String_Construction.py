def con(s):
    ans,count = set(),0
    for i in s:
        if i not in ans:
            count += 1
        ans.add(i)
    return count

print(con("abcabc"))
print(con("abcd"))
print(con("abab"))



