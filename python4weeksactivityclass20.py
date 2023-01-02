class A:
    def __init__(self):
        print("A init executed")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init executed")
abc = B()
'''def func(a,b):
    print(a,b)
def func():
    print("wat!")
func(1,2)
there is no overloading/overlaping in python'''
class A:
    def __init__(self):
        print("A init executed")

class B(A):
    def __init__(self):
        print("B init executed")
abc = B()
'''super is a keyword which helps us access the method of the base class'''
'''MRO(method resolution model'''
class A:
    pass
class B(A):
    pass
class C(B):
    x = 5
class D(A):
    x = 10
class E(C,D):
    pass
e = E()
print(e.x)

class A:
    pass
class B(A):
    pass
class C(B):
    pass
class D(A):
    x = 10
class E(C,D):
    pass
e = E()
print(e.x)

class A:
    x = 5
    pass
class C(B):
    pass
class D(A):
    x = 10
class E(C,D):
    pass
e = E()
print(e.x)
print(E.mro())
'''-DFS
- if there is a loop solve branches diffrently'''
'''Iteration protocal says that for every object to be an iterable for any
object to be an iterable
----For any object to be an iterable,it should have 2 dunders
- __iter__
- __next__'''
#protocal's
'''#object's '__iter__'method should return an iterator
-operator's '__next__' method should return the new value on every call
-if the iterator reaches the end, it should raise an StopIteration exeception'''
a = range(5)
it = a.__iter__()
it
'''iter dunder returns an iterater which helps me iter it over this iterable''' 
print(it.__next__())
it = a.__iter__()
print(it)
print(it.__next__())
next(it)
a = "jatin"
print(iter(a))
class myrange:
    def __init__(self,n):
        self.n = n

    def __iter__(self):
        return myrange_iterator(self)
class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0
    def __next__(self):
        ret = self.i
        self.i += 1
        if ret <= self.myrange.n:
            raise StopIteration
        return ret
for i in range(5):
    print(i)
a = myrange(5)
it = iter(a)
print(next(it))


