from itertools import combinations
def stones(n,a,b):
    sums = set()
    arr = [a,b]*n
    p = combinations(arr,max(2,n-1))
    for i in p:
        sums.add(sum(i))
        #print(i)
    return sorted(sums)
    
print(stones(2,2,3))
print(stones(3,1,2))
print(stones(4,10,100))