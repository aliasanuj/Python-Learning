#coroutine.py
===========================
def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    while True: 
        name = (yield) 
        if prefix in name: 
            print(name) 
corou = print_name("Dear") 
corou.__next__() 
corou.send("Atul") 
corou.send("Dear Atul")
corou.close()
#Searching prefix:Dear
#Dear Atul
======================
def print_name(prefix): 
    print("Searching prefix:{}".format(prefix)) 
    try :  
        while True: 
                name = (yield) 
                if prefix in name: 
                    print(name) 
    except GeneratorExit: 
            print("Closing coroutine!!") 
corou = print_name("Dear") 
corou.__next__() 
corou.send("Atul") 
corou.send("Dear Atul") 
corou.close() 
#Searching prefix:Dear
#Dear Atul
#Closing coroutine!!
========================
def grep(pattern):
    print("Searching for", pattern)
    while True:
        line = (yield)
        if pattern in line:
            print(line)
search = grep('coroutine')
next(search)
# Output: Searching for coroutine
search.send("I love you")
search.send("Don't you love me?")
search.send("I love coroutines instead!")
# Output: I love coroutines instead!
#Searching for coroutine
I love coroutines instead!
============================
def my_coroutine():
    while True:
        received = yield
        print('Received:', received)
it = my_coroutine()
next(it)             # Prime the coroutine
it.send('First')
it.send('Second')
#Received: First
#Received: Second
================================
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
it = minimize()
next(it)            # Prime the generator
print(it.send(10))
print(it.send(4))
print(it.send(22))
print(it.send(-1))
#10
#4
#4
#-1
================================
