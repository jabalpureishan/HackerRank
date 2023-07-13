tests = int(input(""))
for i in range(tests):
    r = int(input("")) - 1
    array = tuple(map(int, input().split()))
    l=0
    curr = float("inf")
    okay = True
    while(l<r):
        if max(array[l],array[r])>curr:
            okay = False
            break
        if array[l]>array[r]:
            curr = array[l]
            l += 1
        else:
            curr = array[r]
            r -= 1
    if okay:
        print("Yes")
    else:
        print("No")
    
    