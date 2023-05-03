def my_func():
    print("hello from function")


my_func()


def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def my_fun_with_default_value(country="Norway"):
    print("I am from " + country)


my_fun_with_default_value()
my_fun_with_default_value("Sweden")


def function(food):
    for x in food:
        print(x)


fruits = ["apple", "grape", "mango"]
function(fruits)
function("apple")
function(range(5))


def return_function(x):
    return x * 2


print(return_function(5))

x = lambda a: a * a
print(x(5))

c = lambda a, b: a * b
print(c(6, 9))

car = ["bmw", "toyota", "audi"]
print(type(car))


