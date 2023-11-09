string = input()
length = len(string)
ans = ind = 0
while ind+3<=length:
    curr = string[ind:ind+3]
    #print(curr)
    if curr[0]!="S":
        ans += 1
    if curr[1]!="O":
        ans += 1
    if curr[2]!="S":
        ans += 1
    ind += 3
print(ans)
