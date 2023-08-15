def larrysArray(A):
    new = sorted(A):
    count = 0
    for i in range(len(A)):
        if A[i]!=new[i]:
            count += 1
    if count%3==0:
        return "YES"
    return "NO"
