thisdict = {
    "brand": "Ford",
    "year": 1964,
    "model": "Mustang"
}
print(thisdict)
print(thisdict["brand"])
print(len(thisdict))

car = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(car)
print(type(car))
x = car.keys()
print(x)
car["colors"] = "white"
print(car)
print(car.values())
print(car.items())

if "brand" in car:
    print("Yes, 'brand' is one of the keys in the thisdict dictionary")

car.update({"year": 2020})
print(car)

car.pop("electric")
print(car)

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

myfamily = {
    "child1" : {
        "name" : "Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobias",
        "year" : 2007
    },
    "child3" : {
        "name" : "Linus",
        "year" : 2011
    }
}
print(myfamily)
child1 = {
    "name" : "Emil",
    "year" : 2004
}
child2 = {
    "name" : "Tobias",
    "year" : 2007
}
child3 = {
    "name" : "Linus",
    "year" : 2011
}

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)
print(myfamily["child2"]["name"])