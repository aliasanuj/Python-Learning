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
