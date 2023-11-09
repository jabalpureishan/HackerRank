tests = int(input())
for i in range(tests):
    length,allowed = map(int,input().split())
    arr = tuple(map(int,input().split()))
    if allowed>=len(list(filter(lambda x:x< =0,arr))):
        print("YES")
    else:
        print("NO")