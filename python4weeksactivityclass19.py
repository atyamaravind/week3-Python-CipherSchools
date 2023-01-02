object
a = 5
print(isinstance(a,object))
a + 4
type(int)
print(isinstance(a,int))
'''is python dynamicly typed language or a compiled language
ans:dynamicly typed language'''

class A:
    pass
print(type(A))
a = 5
def func():
    pass
print(type(func))
print(isinstance(func, object))
class A:
    name = "jatin"
    marks = 50
print(type(A))
A = 5
print(type(A))

print(type(int))
'''int is also a class
class is a way of  defining type
and type is an actual base class list
1.type
2.class== acts like a statement
oops= is big syntax type
'''
print(type(object)) #datatype
class A:
    def __call__(self):
        print("You called me")
a = A()
print(type(a))
a()
b = A.__call__(A)

class A:
    pass
b = A.__call__()
b = A()
def func():
    print("Hello")
func()
func.__call__()
for i in range(5):
    print(i)
'''APIS'''
a = {"name":"Jatin"}
print(a["name"])
class Exponent:
    def __init__(self,n):
        self.n = n
    def __gentiten__(self,x):
        returnx ** self.n
        '''def __init__(self,n):
        self.n = n
    def __gentiten__(self,x):
        returnx ** self.n === API'''
'''e = Exponent(3)
e[6]'''
class A:
    name = "jathin"
    def __init__(self, n):
        self.n = n
a = A(2)
print(a.name)
print(a.n)
'''class A:
    name = "jathin"
    def __init__(self, n):
        this _> n = n
a = A(2)
print(a.name)
print(a.n)'''

class Dog:
    kind = 'canine'
    def __init__(self, name):
        self.name = name
a = Dog("Maxx")
a.name
a.kind
'''class Dog:
    tricks = []
    def __int__(self,name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)
d1 = Dog("Maxx")
d1.add_trick("fetch")
d1.add_trick("talk")
d1.trick
d2 = Dog("Bella")
d2.tricks
a =[]
b=a
b.append(1)'''
