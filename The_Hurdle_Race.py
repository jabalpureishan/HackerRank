lenght,k = map(int,input().split())
arr = tuple(map(int,input().split()))
print(max(0,max(arr)-k))