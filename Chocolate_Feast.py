def choc(n,c,m):
    wrappers = n//c
    total = wrappers
    while(wrappers>=m):
        #print("wrappers:",wrappers)
        curr = wrappers//m
        total += curr
        wrappers -= m*curr 
        wrappers += curr
    return total

print(choc(15,3,2))
print("------------")
print(choc(10,2,5))
print("------------")
print(choc(12,4,4))
print("------------")
print(choc(6,2,2))