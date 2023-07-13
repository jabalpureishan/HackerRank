t = int(input(""))
d = {}
for i in range(t):
    s = input("")
    d[s] = d.get(s,0) +1 
print(len(d))
for i in d:
    print(d[i],end=" ")
