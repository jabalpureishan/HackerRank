    tests = int(input())
    for i in range(tests):
        n = int(input())
        d = {}
        for j in range(n):
            string = sorted(input())
            for k in range(len(string)):
                d[k] = d.get(k,"") + string[k]
        ans = "YES"
        for j in d:
            if d[j]!="".join(sorted(d[j])):
                ans = "NO"
                break
        print(ans)



    