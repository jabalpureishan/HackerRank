
def steadyGene(gene):
    d = {"G":0,"T":0,"A":0,"C":0}
    length = len(gene)//4
    for i in gene:
        d[i] += 1
    count = 0
    for i in d.values():
        if i<length:
            count += length - i
    return count

print(steadyGene("GAAATAAA"))
