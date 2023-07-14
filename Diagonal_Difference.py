def diff(ar):
    first = second = 0
    j = n - 1
    for i in range(n):
        first += ar[i][i]
        second += ar[i][j]
        j -= 1
    return abs(first - second)
