length = int(input())
arr = list(map(int,input().split()))
arr.sort()
Min = float("inf")
for i in range(1,length):
    Min = min(Min,arr[i]-arr[i-1])
print(Min)