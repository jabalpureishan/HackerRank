from  collections import Counter
    
def anagram(arr):

    def check(d1,d2):
        for i in d2:
            if d2[i]>d1.get(i,0):
                return False
        return True


    grams,count = [],0
    arr.sort(reverse=True,key=lambda x:len(x))
    for i in arr:
        temp = Counter(i)
        for j in grams:
            if check(j,temp):
                count += 1
        grams.append(temp)

    return count

print(anagram(["cat","dog","tac","god"]))

print(anagram(["listen","silent","hello","world","herlwdlo"]))
