#coroutine.py


#############################################################################
# 1. coroutines : Couroutines are similar to generator but with few extramethods and slight change in how we use yield statement.
# 2. Generator produces data for iteration while coroutines can also consume data.
# 3. Execution of coroutine is similar to generator. When we call coroutine nothing happens.
# 4. It runs only in response to next() and send() methods.
# 5. Closing coroutine : Coroutine might run indefinately to close coroutine close() method is used.
# 6. When coroutine is close it generate GenerateExit exception which can be done in usual way.
# 7. If we try to send value after closing coroutine, it will raise StopIteration exception.
#############################################################################




#############################################################################
# def name(prefix):
#   print("searchimg prefix {} ".format(prefix))
#   while True:
#     y = yield
#     if prefix in y:
#       print(y)
# obj = name("anuj")
# obj.__next__()
# obj.send("anuj")
# obj.send("Anuj anuj")
# obj.send("anuj kumar")
# obj.send("kumar anuj")
# obj.close()
# #searchimg prefix anuj
# #anuj
# #Anuj anuj
# #anuj kumar
# #kumar anuj





#############################################################################
# def print_name(prefix):
#     print("Searching prefix:{}".format(prefix))
#     while True:
#         name = (yield)
#         if prefix in name:
#             print(name)
# corou = print_name("Dear")
# corou.__next__()
# corou.send("Atul")
# corou.send("Dear Atul")
# corou.close()
# #Searching prefix:Dear
# #Dear Atul




#############################################################################
# def outer(parameter):
#   print("the requested word is {}".format(parameter))
#   while True:
#     x = yield
#     if parameter in x:
#       print(x)
# obj = outer("anuj")
# obj.__next__()
# obj.send("anuj")
# obj.send("kumar anuj")
# obj.send("kumar Anuj")
# obj.close()
# #the requested word is anuj
# #anuj
# #kumar anuj



#############################################################################
# def outer(searching):
#     print("searching for {}".format(searching))
#     while True:
#         y = yield
#         if searching in y:
#             print(searching)
# obj1 = outer("anuj")
# obj1.__next__()
# obj1.send("Anuj")
# obj1.send("Anuj anuj")
# obj1.send("Anuj kumar")
# obj1.send("anuj Anuj")
# obj1.close()
# searching for anuj
# anuj
# anuj




#############################################################################
# def print_name(prefix):
#     print("Searching prefix:{}".format(prefix))
#     try :
#         while True:
#                 name = (yield)
#                 if prefix in name:
#                     print(name)
#     except GeneratorExit:
#             print("Closing coroutine!!")
# corou = print_name("Dear")
# corou.__next__()
# corou.send("Atul")
# corou.send("Dear Atul")
# corou.close()
# #Searching prefix:Dear
# #Dear Atul
#Closing coroutine!!




#############################################################################
# def grep(pattern):
#     print("Searching for", pattern)
#     while True:
#         line = (yield)
#         if pattern in line:
#             print(line)
# search = grep('coroutine')
# next(search)
# # Output: Searching for coroutine
# search.send("I love you")
# search.send("Don't you love me?")
# search.send("I love coroutines instead!")
# Output: I love coroutines instead!
#Searching for coroutine
#I love coroutines instead!



#############################################################################
# def my_coroutine():
#     while True:
#         received = yield
#         print('Received:', received)
# it = my_coroutine()
# next(it)             # Prime the coroutine
# it.send('First')
# it.send('Second')
#Received: First
#Received: Second




#############################################################################
# def minimize():
#     current = yield
#     while True:
#         value = yield current
#         current = min(value, current)
# it = minimize()
# next(it)            # Prime the generator
# print(it.send(10))
# print(it.send(4))
# print(it.send(22))
# print(it.send(-1))
#10
#4
#4
#-1




#############################################################################
# def abc(n):
#   print("searching element",n)
#   try:
#     while True:
#       y = yield 
#       if n in y:
#         print(n," is there")
#   except GeneratorExit:
#     print("stopped")
# obj1 = abc("anuj")
# obj1.__next__()
# obj1.send("kumar Anuj")
# obj1.send("anUj")
# obj1.close()
#searching element anuj
#stopped

