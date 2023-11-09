lenght = int(input())
string = input()
special = "!@#$%^&*()-+"
add = 4
lo = up = di = sp = False
for i in string:
    if i.isalpha():
        if i.islower():
            lo = True
        else:
            up = True
    elif i.isnumeric():
        di = True
    elif i in special:
        sp = True
if sp:
    add -= 1
if lo:
    add -= 1
if up:
    add -= 1
if di:
    add -= 1
print(max(6-lenght,add))