"""from math import floor,log
def palindrome(n):
    def method1(n):
        temp = n
        rev = 0
        power = floor(log(n,10)+1)-1
        while(n>0):
            rev += (n%10)*(10**power)
            power -= 1
            n //= 10
        return rev==temp

    def method2(n):
        n = str(n)
        return n==n[::-1]

    print("using method 1:",method1(n))
    print("using method 2:",method2(n))
    return ""

print(palindrome(121))
print(palindrome(9563))"""
from math import ceil,tan,pi,radians,floor
radius = 10*tan(radians(30))
area = 3.14*(radius**2)
print(floor(area))