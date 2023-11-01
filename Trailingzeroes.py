from math import factorial
def trailing(n):
    num = factorial(n)
    count = 0
    while num%10==0 :
        count += 1
        num //= 10
    return count
def efficient(n):
    num,count = 5,0
    while(num<=n):
        count += n//num
        num *= 5
    return count

print(trailing(100),efficient(100))
print(trailing(200),efficient(200))