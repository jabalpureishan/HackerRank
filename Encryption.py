from math import ceil,floor,sqrt
def encryption(s):
    new = ""
    length = 0
    for i in s:
        if i.isalpha():
            length += 1
            new += i
    root = sqrt(length)
    rows = int(floor(root))
    columns = int(ceil(root))
    #print("before: rows:",rows,"columns:",columns)
    while(rows*columns<length):
        if rows>=columns:
            columns += 1
        else:
            rows += 1
    #print("aftre: rows:",rows,"columns:",columns)
    output = ""
    for i in range(columns):
        #print("i:",i)
        start = i
        curr = ""
        for j in range(rows):
            if start>=length:
                continue
            curr += new[start]
            #print("start:",start,"letter:",new[start])
            start += columns
        output += curr + " "
    return output

print(encryption("if man was meant to stay on the ground god would have given us roots"))
print(encryption("haveaniceday"))
print(encryption("feedthedog    "))
print(encryption("chillout"))      
