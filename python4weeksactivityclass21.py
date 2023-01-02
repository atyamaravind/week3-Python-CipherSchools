'''Generators
concept between lagy loading and egar loading
Genetors is a concept in python which helps us to generate values on the fly
This is a way in python in which we achieve lazy loading so to say and in a more
intermediate or advanced manner these some have endup writing parallel code as well.
corotines ==it is the programmer that the who giveaway the control of the given function in
the case of corotines
so thats what generators are..'''
'''def generate_squares(n):
a = []
for i in range(1,100):  #in range we can give a starting point
    a.append(i**2)
    return a'''
#Egar Loading
def generate_squares(n):
    return [i**2 for i in range(1,n) ]
for x in generate_squares(100):
    print(x)

#keyword: yield
#Lagy Loading
def generate_squares(n):
    for i in range(1,n):
        yield i**2

for i in generate_squares(10):
    print(i)
it = iter(generate_squares(10))
print(it)
print(next(it))
def func():
    print("start")
    yield 1
    print("yielded 1")
    yield 2
    print("yielded 2")
it = iter(func())
print(it)
next(it)
print("hello")
#for i in range(10000000000):
'''for i in range(10000000000):
                                            pass
                                            ==defering'''
pass
print("world")

from time import sleep
def func():
    print("started")
    yield
    sleep(5)
    print("ended")
print("hello")
it = iter(func())
print(next(it))
print("world")
#print(next(it))
a = generate_squares(10)
print(type(a))

for i in generate_squares(10):
    print(i)
a = (i**2 for i in range(10))
print(type(a))
for i in a:
    print(i)
for i in a:
    print(i)
'''A generator is nothing but an iterator on which you know iterate the values '''
a = generate_squares(10)
print(next(a))
'''An iterator can only iterate once
if the iterator reaches the end it can't iterate further
'''
a = (i**2 for i in range(10))
for i in a:
    print(i)
    '''a = (i**2 for i in range(10))
for i in a:
    print(i) we can iterate iterate it once'''
a = (i**2 for i in range(10))
print(iter(a))
print(a)
'''the actual use case  of generator is to giving away the control
is to run the code in a lagy loading model'''
a = (i**2 for i in range(10))
next(a)
next(a)
for i in a:
    print(i)
