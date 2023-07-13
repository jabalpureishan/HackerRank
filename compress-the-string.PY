s = input("")
s += "#"
count = 0
prev = s[0]
for i in range(len(s)):
    if s[i]==prev:
        count += 1
    else:
        out = (count,int(prev))
        print(out,end=" ")
        count = 1
        prev = s[i]


