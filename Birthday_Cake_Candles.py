n = int(input())
arr = list(map(int,input().split()))
Max = arr[0]
d = {}
for i in arr:
    Max = max(Max,i)
    d[i] = d.get(i,0) + 1
print(d[Max])
