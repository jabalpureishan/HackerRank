albets = "abcdefghijklmnopqrstuvwxyz"
d,ind = {},0
for i in albets:
    d[i] = ind
    ind += 1
length = int(input())
string = input()
shift = int(input())
ans = ""
for i in string:
    if i.isalpha():
        curr = i.lower()
        now = albets[(d[curr]+shift)%26]
        if i.isupper():
            ans += now.upper()
        else:
            ans += now
    else:
        ans += i
print(ans)