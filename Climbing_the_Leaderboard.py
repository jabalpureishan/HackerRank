def climbing(ranked,player):
    
    out = []
    newrank = []
    set_ = set()
    for i in ranked:
        if i not in set_:
            newrank.append(i)
            set_.add(i)
    length = len(newrank)
    start = 0
    for i in player:
        if i>newrank[0]:
            out.append(1)
        else:
            for j in range(length-1,start-1,-1):
                print("j:",j,newrank[j])
                if newrank[j]>=i:
                    start = j
                    out.append(j+1)
                    break
            else:
                out.append(length+1)
    return out




print(climbing([100,90,90,80],[70,80,105]))
print(climbing([100,100,50,40,40,20,10],[5,25,50,120]))