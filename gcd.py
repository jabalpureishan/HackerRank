from math import gcd
def hcf(num1,num2):

    def naive(num1,num2):
        Min = min(num1,num2)
        for i in range(Min,0,-1):
            if num1%i==0 and num2%i==0:
                return i

    def library(num1,num2):
        return gcd(num1,num2)

    def euclid(num1,num2):
        while num1!=num2:
            if num1>num2:
                num1 -= num2
            else:
                num2 -= num1
        return num1
    
    def opteuclid(num1,num2):
        if num2==0:
            return num1
        return opteuclid(num2,num1%num2)

    return naive(num1,num2),library(num1,num2),euclid(num1,num2),opteuclid(num1,num2)


    

print(hcf(12,12))
print(hcf(1560,1890))


