def game(s):
    odd,d = 0,{}
    for i in s:
        d[i] = d.get(i,0) + 1
    for i in d.values():
        if i&1==1:
            odd += 1
    if odd>=2:
        return "NO"
    return "YES"
    