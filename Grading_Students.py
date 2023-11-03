from math import ceil
tests = int(input())
for i in range(tests):
    num = int(input())
    if num<38:
        print(num)
    else:
        next = ceil(num/5)*5
        if next-num<3:
            print(next)
        else:
            print(num)

actual = []  
for i in range(6):
    curr = [i]*len(img_arr[i])
    actual.append(curr)
print(actual)

test_values = []
for i in img_arr:
    for j in i:
        test_values.append(model_predict(j,model))
cm = confusion_matrix(actual,test_values)
