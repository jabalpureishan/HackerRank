def red(s):
    while(True):
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                s = s[:i-1] + s[i+1:]
                break
        else:
            break
    if s=="":
        return "Empty String"
    return s

print(red("aaabccddd"))
print(red("aa"))
print(red("baab"))