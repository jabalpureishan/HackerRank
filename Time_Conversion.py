s = input()
num = int(s[:2])
if s[-2:]=="PM":
    if num==12:
        pass
    else:
        s = str(num+12) + s[2:]
else:
    if num==12:
        s = "00"+s[2:]

s = s[:-2]
print(s)