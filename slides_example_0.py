#!/usr/bin/python3def foo():    a = 0    while True:        return a        a += 1  # this doesn't do anythingprint("Foo()")print(foo())for i in range(10):    print(foo())#***********************************************************************************************************************def bar():    a = 0    while True:        yield a        a += 1print("Bar()")print(bar())my_gen = bar()for i in range(10):    print(next(my_gen))for i in bar():    print(i)