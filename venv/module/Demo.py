import mymodule
import mymodule2 as mm
import platform
from person import person1

mymodule.greeting()
mm.greeting()

x = platform.system()
print(x)

d = dir(platform) # all function and variables in module
print(d)

print(person1)