def divisors(num):

    def naive(num):
        arr = []
        for i in range(1,num+1):
            if num%i==0:
                arr.append(i)
        return arr

    def better(num):
        arr = []
        i = 1
        while i*i<=num:
            if num%i==0:
                arr.append(i)
                if i!=num//i:
                    arr.append(num//i)
            i += 1
        return arr

    return naive(num),better(num)

print(divisors(30))