from math import gcd
def lcm(a,b):

    mult = a*b

    def naive(a,b):
        Max = max(a,b)
        while Max%a!=0 or Max%b!=0:
            Max += 1
        return Max

    def library(a,b):
        return mult//gcd(a,b)

    def euclid(a,b):
        while a!=b:
            if a>b:
                a -= b
            else:
                b -= a
        return mult//a

    def opteuclid(a,b):
        if b==0:
            return mult//a
        return opteuclid(b,a%b)

    return naive(a,b),library(a,b),euclid(a,b),opteuclid(a,b)

print(lcm(12,15))
print(lcm(3,7))