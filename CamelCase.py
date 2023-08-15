def camelcase(s):
    count = 0
    for i in range(1,len(s)):
        if s[i].isupper():
            count += 1
    return count + 1
