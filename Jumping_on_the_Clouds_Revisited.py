length,jump = map(int,input().split())
arr = tuple(map(int,input().split()))
count = max(1,3*arr[0])
curr = jump
while curr%length>0:
    count += 1
    if arr[curr%length]==1:
        count += 2
    curr += jump
print(100-count)
