tests = int(input(""))
array = []
for i in range(tests):
    x,y = input().split()
    y = int(y)
    if x=="r":
        if len(array)==0:
            print("Wrong!")
            continue
        else:
            array.remove(y)
    else:
        array.append(y)
    array.sort()
    #print("array:",array)
    length = len(array)
    if length==0:
        print("Wrong!")
        continue
    if length%2==0:
        print(round((array[length//2]+array[(length//2)-1])/2,1))
    else:
        print(array[(length-1)//2])
