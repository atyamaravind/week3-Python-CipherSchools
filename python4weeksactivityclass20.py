'''class A:
    def __init__(self, x):
        self.x = x

class B(A):
    pass
abc = B()'''

class A:
    def __init__(self, x):
        print("A init executed")
class B(A):
    def __init__(self):
        print("B init executed")
abc = B()
'''***python doesn't have the concept of over loading'''

'''def func(a,b):
    print(a,b)

def func():
    print("wat!")

func(1,2)'''
'''python doesn't have polymorphic functions by design& by design python doesn't support
the polymorphism
init is not a constructor'''
'''class A:
    def __init__(self, x):
        print("A init executed")
class B(A):
    def __init__(self):
       print("B init executed")
       super().__init__()
abc = B()'''
'''MRO(Method Resolution Order)'''
class A:
   pass
class B(A):
    pass
class C(B):
    x = 5
class D(A):
    x = 10
class E(C, D):
    pass
e = E()
print(e.x)
print(E.mro())
'''-DFS
-if there is a loop solve the branches differently'''
'''dunders,iterators,iterables'''
'''iteration protocal in python says that for every object to be iterable it should
have 2 dunders
-__iter__
-__next__
protocal
-object's __iter__ method should return an iterator
-iterator's __next__ method should return the new value on every call
-if the iterator reaches the end ,it should raise an StopIteration exception'''
a = range(5)
it = a.__iter__()
print(type(it))
'''iter dunder returns an iterator which helps me iterate it over this iteretor'''
it.__next__()
it = a.__iter__()
print(it)
it = it.__next__()
print(it)
#it = it.__next__()
#print(it)
#next(it)
class myrange:
    def __int__(self,n):
        self.n = n
    def __int__(self):
        return myrange_iterator(self) 
class myrange_iterator:
    def __init__(self, myrange):
        self.myrange = myrange
        self.i = 0
    def __next__(self):
        ret = self.i
        self.i += 1

        if ret >= self.myrange.n:
            raise StopIteration

        return ret
for i in myrange(5):
    print(i)
