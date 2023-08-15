def matchingStrings(stringList, queries):
    d,out = {},[]
    for i in stringList:
        d[i] = d.get(i,0) + 1
    for i in queries:
        out.append(d.get(i,0))
    return out