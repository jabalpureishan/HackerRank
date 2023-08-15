def alternate(s):
    chars,Max = tuple(set(s)),0
    length = len(chars)
    for i in range(length):
        for j in range(i+1,length):
            curr = ""
            #print("to have:",chars[i],chars[j])
            for k in s:
                if k==chars[i] or k==chars[j] :
                    if len(curr)!=0 and curr[-1]==k:
                        break
                    else:
                        curr += k
            else:
                print(curr)
                Max = max(Max,len(curr))
    return Max



print(alternate("abaacdabd"))
print("---------------")
print(alternate('beabeefeab'))
print("---------------")
print(alternate("asdcbsdcagfsdbgdfanfghbsfdab"))
print("---------------")

