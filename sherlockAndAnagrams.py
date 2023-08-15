def sherlockAndAnagrams(s):
    d = {}
    length = len(s)
    for i in range(1,length):
        window = i
        slides = length - window + 1
        for j in range(slides):
            curr = "".join(sorted(s[j:window]))
            d[curr] = d.get(curr,0) + 1
            window += 1
    output = 0
    for i in d.values():
        i -= 1
        output += (i*(i+1))//2
    return output
print(sherlockAndAnagrams("kkkk"))
print(sherlockAndAnagrams("cdcd"))
print(sherlockAndAnagrams("ifailuhkqq"))
print(sherlockAndAnagrams("abba"))
print(sherlockAndAnagrams("abcd"))