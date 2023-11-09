budget,usbs,keyboards = map(int,input().split())
usbprice = tuple(map(int,input().split()))
kbprice = tuple(map(int,input().split()))

Max = -1
for i in range(usbs):
    for j in range(keyboards):
        Sum = usbprice[i]+kbprice[j]
        if Sum<=budget:
            Max = max(Max,Sum)
print(Max)

