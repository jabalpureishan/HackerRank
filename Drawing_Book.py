last = int(input())
reach = int(input())
if last%2!=0:
    last -= 1
if reach%2!=0:
    reach -=1 
if reach==last:
    print(0)
else:
    print(min(reach//2,(last-reach)//2))