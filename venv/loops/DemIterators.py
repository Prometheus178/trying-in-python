mytuple = ("apple", "banana", "cherry", None)
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


class MyIterableClass:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myIterable = MyIterableClass()
myIter = iter(myIterable)
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
# print(next(myIter)) #you will get StopIterationExceprtion
