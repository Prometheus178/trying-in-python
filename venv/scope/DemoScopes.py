#local scope
def my_func():
    x = 300
    global y
    y = 400
    print(x)
    def inner_func():
        print(x)
    inner_func()

my_func()

#global scope
a = 100 # available in any scope
x = 200

print(x)
print(y)
