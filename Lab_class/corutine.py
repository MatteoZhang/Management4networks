# routine
def foo():
    a = 0  # start of the routine enter
    while True:
        return a  # terminate the code exit
        a += 1

print("Foo()")
print(foo())

for i in range(10):
    print(foo())

def bar():  # corutine generator object
    a = 0
    while True:
        yield a  # when we have yield then bar is an object
        a += 1

print("Bar()")
print(bar())

for i in range(10):
    print(bar())

my_generator = bar()  # lazy evaluation if u don't need it u don't use it
for i in range(10):  # return the value only if needed
    print(next(my_generator))  # suspend the function and then continue

for i in bar():
    print(i)
    if i == 500:
        break
