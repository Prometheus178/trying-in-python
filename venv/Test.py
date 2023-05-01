
# print("hello world!")
x = "5"
print(type(x))
y = 6
print(type(y))
z = float(7)
print(z)
x, y, z = 1, 6.0, "7"
print(x, y, z)
w = {1, 3, 3, 4, 5}
print(w)
q = [1, 3, 4, 5, 5]
print(q)

word = "hello"
print(word[1])  # e

for x in word:
    print(x)

print(x)  # o

print(len(word))

txt = "The best things in life are free!"
print("best" in txt)  # True

if ("the" in txt):
    print("yes, its exist")
else:
    print("No, I can't find")

txt = "The best things in life are free!"
print("expensive" not in txt)

b = "Hello, World!"
print(b[2:5])
print(len(b))
print(b[0:120])  # there is no out of bounce
print(b[:9])
print(b[5:])

c = "World"
print(c[-5:])

a = " Hello, World! "
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace('W', 'H').strip())
print(a.strip().split(","))

a = "Hello"
b = "World"
c = a + b
print(c)
print(a + " " + b)

age = 36
txt = "My name is John, and I am {} old"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

txt = "We are the so-called \"Vikings\" from the north."
print(txt)
print(txt.count("e"))

print(bool("Hello"))  # true
print(bool(""))  # false
print(bool(" "))  # true
print(bool(15))  # true
print(bool(0))  # false

print(3 ** 3)

print(4 >> 1)  # 2
print(4 >> 2)  # 1
print(7 >> 1)  # 3
print(10 >> 1)  # 5

print(4 << 1)  # 8
print(4 << 2)  # 16
print(7 << 1)  # 14
print(10 << 1)  # 20

print(type(40000000000))  # int
print(x)  # o where x is the global value
print(isinstance(x, int))
if (x != "O"):
    print(True)

