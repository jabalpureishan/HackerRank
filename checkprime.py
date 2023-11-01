def prime(num):

    def naive(num):
        if num==1:
            return False
        for i in range(2,num):
            if num%i==0:
                return False
        return True


    def better(num):
        i = 2
        while i*i<=num:
            if num%i==0:
                return False
            i += 1
        return True

    def best(num):
        if num==1:
            return False
        if num==2 or num==3:
            return True
        if num%2==0 or num%3==0:
            return False
        i = 5
        while i*i<=num:
            if num%i==0 or num%(i+2)==0:
                return False
            i += 6
        return True

    return naive(num),best(num),better(num)
print(prime(16))
