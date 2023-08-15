def arrayManipulation(n, queries):
    array,Max,Sum = [0]*n,0,0
    for i in queries:
        array[i[0]-1] += i[2]
        if i[1]<n:
            array[i[1]] += -i[2]

    #print(array)
    for i in array:
        Sum += i
        Max = max(Max,Sum)
    return Max
    
print(arrayManipulation(10,[[1,5,3],[4,8,7],[6,9,1]]))