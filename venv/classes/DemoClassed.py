class MyClass:
    x = 5


p = MyClass()
print(p.x)


class Person:
    # self it's like 'this' in Java , extra you can give him any name and it will work as usual
    def __init__(self, name, age):  # this is kind of constructor
        self.name = name
        self.age = age

    def __str__(self):  # this is kind of toString
        return f"{self.name} + ({self.age})"

    def sayHello(self):
        print("Hello, my name is " + self.name)


p1 = Person("Jack", 16)
print(p1)
print(p1.name)
print(p1.age)
p1.sayHello()
del p1.age
# print(p1.age) you will get the error cuz of above we deleted property 'age' in instance
del p1


# print(p1) get error


class Person:
    def __init__(self, name, lastName):
        self.name = name
        self.lastName = lastName

    def __str__(self):
        return f"{self.name} {self.lastName}"

person = Person("John", "Dow")
print(person)

class Student(Person):
    pass

student = Student("Jown", "Lewinsky")
print(student)

class Student(Person):
    def __init__(self, fName, lName, graduationYear):
        super().__init__(fName, lName)
        self.graduationYear = graduationYear

s1 = Student("Jack" , "Sally", 2023)
print(s1)
print(s1.graduationYear)
