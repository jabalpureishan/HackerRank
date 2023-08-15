def getMoneySpent(keyboards, drives, b):
    Max = -1
    for i in keyboards:
        for j in drives:
            if i+j<=b:
                Max = max(Max,i+j)
    return Max

print(getMoneySpent([40,50,60],[5,8,12],60))
print(getMoneySpent([3,1],[5,2,8],10))
print(getMoneySpent([4],[5],5))