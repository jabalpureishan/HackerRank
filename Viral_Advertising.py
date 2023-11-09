
num = int(input())
Sum = 0
curr = 5
for i in range(num):
    likes = curr//2
    Sum += likes
    curr = likes*3
print(Sum)