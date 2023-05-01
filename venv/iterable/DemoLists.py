list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)

list1 = ["abc", 34, True, 40, "male"]
print(list1)
print(type(list1))

thisList = ["apple", "banana", "cherry"]
print(thisList[-1])
print(thisList[-3])
print(thisList[0])
# print(thisList[-4]) out of range
thisList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thisList[2:5])
print(thisList[2:])
print(thisList[-4:])
print(thisList[-4:-1])

if 'apple' in thisList:
    print("Yes, 'apple' is in the fruits list")

thisList1 = ["apple", "banana", "cherry"]
thisList1[-1] = "blackcurrant"
print(thisList1)

thisList2 = ["apple", "banana", "cherry"]
thisList2[0:2] = ["blackcurrant", "watermelon"]
print(thisList2)

thisList3 = ["apple", "banana", "cherry"]
thisList3.insert(1, "watermelon")
print(thisList3)
thisList3.append("orange")
print(thisList3)
thisList4 = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thisList4.extend(tropical)
print(thisList4)
thisList5 = ["apple", "banana", "cherry"]
thisTuple = ("kiwi", "orange")
thisList5.extend(thisTuple)
print(thisList5)

print(thisList5.remove("banana"))
print(thisList5)
print(thisList5.pop(2))
print(thisList5)
print(thisList5.pop())  # take the last item
print(thisList5)
del thisList5[1]
print(thisList5)
thisList5.clear()
print(thisList5)
del thisList5  # removed the whole list

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

[print(x) for x in thislist]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [expression for item in iterable if condition == True]
newFruitList = [x for x in fruits if "a" in x]
print(newFruitList)
newlist = [x for x in fruits if x != "apple"]
print(newlist)
newlist = [x for x in fruits]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)
newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)


thislist = ["banana", "orange", "Kiwi", "Cherry"]
thislist.sort()
print(thislist)

thislist.sort(key = str.lower)
print(thislist)

thislist.reverse()
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
mylist = list(thislist)
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
list1.extend(list2)
print(list1)