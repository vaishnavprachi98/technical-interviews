"""
@author: David Lei
@since: 23/08/2016
@modified: 

http://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python

Exploring what the key word yield does

need to understand
    1. iterators
    2. generators
in that order

Iterables
Things that are iterable are things that you can use "for... in...." (strings, lists, files, etc)

Generators
Are iterators, but you can only iterate over them once because they do not store the value in memory
--> generate values on the fly

below example, generator calculate 0 then forgets about it then calculates 1 then 4 one by one

Yield
is a keyword used like return except the function will return a generator
"""

myGenerator = (x*x for x in range(3))
for i in myGenerator:
    print("first try: " + str(i))
    print(myGenerator)

for j in myGenerator:               # wont print anything
    print("second try: " + str(j))

print("Playing with yield")

def createGenerator():
    myList = range(3)
    for i in myList:
        yield i*i

anotherGenerator = createGenerator()
print(anotherGenerator)
for i in anotherGenerator:
    print(i)

"""
above example is kinda useless, but generators are good when you know your function will
return a huge set of values that you will only need to read once

when you call the function, the code you have in the function body doesn't run, the function only return the generator
object

then your code will be run each time the for uses the generator. The first time the for calls the
generator object created in your function, it will run the code in your function from beginning until it hits yeild, then
it will return the first value of the loop, Each other call will run the loop in the function once more and return the
next value until there is no value to return

refer to stack overflow link to learn more.
"""