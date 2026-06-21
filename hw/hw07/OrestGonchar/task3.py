word = input('Enter word')
mydict = {}
for w in word:
    if w in mydict:
        mydict [w] += 1
    elif w not in mydict:
        mydict[w] = 1
print(mydict)