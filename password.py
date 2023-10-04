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

print(list)

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
    newarray = []
    for i in range(len(array)):
        newarray.append("0")
    while newarray!=array:
        for i in range(len(array)):
            newarray[i] = list[r.randint(0,len(list)-1)]
    print(arraytostr(newarray))

password = []


for i in range(5):
    password.append(list[r.randint(0,len(list)-1)])
print(arraytostr(password))

tryto2(password)
