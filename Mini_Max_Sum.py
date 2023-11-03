arr = sorted(list(map(int,input().split())))
sum_ = sum(arr[:4]) 
print(sum_,sum_-arr[0]+arr[-1])