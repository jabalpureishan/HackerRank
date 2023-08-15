def twostr(s1,s2):
    s1 = set(s1)
    for i in s2:
        if i in s1:
            return "YES"
    return "NO"
