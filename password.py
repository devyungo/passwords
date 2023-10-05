import random as r
import string as s


list = list(s.ascii_letters)

newlist = []
for i in range(10):
    newlist.append(f"{i}")

list.extend(newlist)
list.extend(newlist)
list.extend(newlist)
list.extend(newlist)

r.shuffle(list)


def arraytostr(array):
    string = ""
    for i in range(len(array)):
        string+=array[i]
    return string

def tryto(array):
    tryarray = []
    for i in range(len(array)):
        tryarray.append("0")
    while tryarray!=array:
        for i in range(len(array)):
            while tryarray[i]!=array[i]:
                tryarray[i] = list[r.randint(0,len(list)-1)]
            print(arraytostr(tryarray))

def tryto2(array):
    tries=0
    newarray = []
    for i in range(len(array)):
        newarray.append("0")
    while newarray!=array:
        for i in range(len(array)):
            newarray[i] = list[r.randint(0,len(list)-1)]
            tries+=1
    return tries

def newpass(value):
    password = []
    for i in range(value):
        password.append(list[r.randint(0,len(list)-1)])
    return password
    
trieslist = []

for i in range(100):
    for i in range(10):
        newtries = tryto2(newpass(3))
        trieslist.append(newtries)
    print(sum(trieslist)/len(trieslist))
    print(i)









