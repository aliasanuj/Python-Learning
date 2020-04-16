#closure.py



########################################################################
# 1. Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.
# 2. A function defined inside another function is called a nested function.
# 3. Nested functions can access variables of the enclosing scope.
# 4. In Python, these non-local variables are read only by default and
# 5. we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them
# ==> A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.
# base concept of decorator is closure
# 6. First class function




########################################################################
# def gen_multiplier(x):
#     def multiplier(y):
#         return x * y
#     return multiplier
# obj = gen_multiplier(10)
# print(obj(5))
#50






########################################################################
# def gen_multiplier(x):
#
#     def multiplier(y):
#         return x * y
#     return multiplier
#
#     def multiplier(y):
#         return x + y
#     return multiplier
#
# obj = gen_multiplier(10)
# print(obj(5))
#15 it wont call the second function. it will calll only immediate function



########################################################################
# def gen_multiplier(x):
#
#     def multiplier(y):
#         return x * y
#     return multiplier
#
#     def multiplier(y):
#         return x + y
#     return multiplier() #it wont reach here
#
# obj = gen_multiplier(10)
# print(obj(5))
#50




# ########################################################################
# def gen_multiplier(x):
#     def multiplier(y):
#         return x * y
#     return multiplier()
# obj = gen_multiplier(10)
# print(obj(5))
#TypeError: multiplier() missing 1 required positional argument: 'y'




# ########################################################################
# def gen_multiplier():
#     x = 10
#     def multiplier(y):
#         return x * y
#     return multiplier
# obj = gen_multiplier()
# print(obj(5))
#50



#########################################################################
# def gen_multiplier():
#     x = 10 #non-local variable
#     def multiplier(y): #stores the reference to non-local variable
#         return x * y #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier()
# del gen_multiplier #it will delete
# print(obj(5))
#50




# ########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print(a+b)
#     return inner
# obj = outer(5)
#5



#########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print(a+b)
#     return inner
# obj = outer(5)
# print(obj(10))
# #5
#15
#none




#########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print(a+b)
#     return inner
# obj = outer(5)
# print(obj(10))
# obj(10)
#5
#15
#None
#15


#########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print(a+b)
#     return inner
# obj = outer(5)
# print(obj(10))
# obj(12)
# 5
# 15
# None
# 17



#########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print(a+b)
#     return inner
# obj = outer(5)
# obj(10)
#5
#15


# #########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print("aaa")
#         print(b)
#         print(a+b)
#     return inner
# obj = outer(5)
# print(obj(10))
# obj(10)
# 5
# aaa
# 10
# 15
# None
# aaa
# 10
# 15



#########################################################################
#def outer(a):
#     print(a)
#     def inner(b):
#         print("aaa")
#         print(b)
#         print(a+b)
#     return inner
# obj = outer(5)
# obj(12)
# obj(15)
# 5
# aaa
# 12
# 17
# aaa
# 15
# 20





#########################################################################
# def outer(a):
#     print(a)
#     def inner(b):
#         print("aaa")
#         print(b)
#         print(a+b)
#     return inner
# obj = outer(5)
# print(obj(10))
# obj(10)
#op :
#5




#########################################################################
# def gen_multiplier(a):
#     x = 10 #non-local variable
#     def multiplier(y): #stores the reference to non-local variable
#         return x * y * a #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier(10)
# del gen_multiplier #it will delete
# print(obj(5))
#500





#########################################################################
# def gen_multiplier(a):
#     x = 10 #non-local variable
#     print(a)
#     def multiplier(y): #stores the reference to non-local variable
#         print(y)
#         return x * y * a #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier(10)
# del gen_multiplier #it will delete
# print(obj(5))
# 10
# 5
# 500




#########################################################################
# def gen_multiplier(a):
#     x = 10 #non-local variable
#     print(a)
#     def multiplier(y): #stores the reference to non-local variable
#         print(y)
#         return x * y * a #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier(12)
# del gen_multiplier #it will delete
# print(obj(5))
# 12
# 5
# 600



#########################################################################
# m = 12
# def gen_multiplier(a):
#     x = 10 #non-local variable
#     def multiplier(y): #stores the reference to non-local variable
#         return x * y * a  #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier(10)
# del gen_multiplier #it will delete
# print(obj(5))
# 500




#########################################################################
# m = 12
# def gen_multiplier(a):
#     x = 10 #non-local variable
#     def multiplier(y): #stores the reference to non-local variable
#         return x * y * a *m #x is non local to multiplier
#     return multiplier
# #call the function
# obj = gen_multiplier(10)
# del gen_multiplier #it will delete
# print(obj(5))
#6000




#########################################################################
# global m
# m = 12
# def gen_multiplier(a):
#     m = 10
#     print(m)
#     print(a)
#     def multiplier(y): #stores the reference to non-local variable
#         return m * y * a #m will be 10 not 12
#     return multiplier
# #call the function
# obj = gen_multiplier(7)
# del gen_multiplier #it will delete
# print(obj(5))
# # 10
# 7
# 350



#########################################################################
# nested-function
# nested function should access non-local variable
# it should return the en-closed function
#########################################################################




#########################################################################
# def print_msg(msg):
# # This is the outer enclosing function
#     def printer():
# # This is the nested function
#         print(msg)
#     return printer()
# # We execute the function
# # Output: Hello
# print_msg("Hello")




#########################################################################
# def print_msg(msg):
#     print("aaa")
#     def printer():
#         print(msg)
#     return printer()
# print_msg("Hello")
# aaa
# Hello




#########################################################################
# def print_msg(msg):
# # This is the outer enclosing function
#     def printer():
# # This is the nested function
#         print(msg)
#     return printer
# # We execute the function
# # Output: Hello
# print_msg("Hello")
#print nothing





#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer # () is required
# print_msg("Hello")
# no output





#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer()
# print_msg("Hello")
#Hello




#########################################################################
# def print_msg(msg):
#     def printer(msg):
#         print(msg)
#     return printer()
# print_msg("Hello")
#TypeError: printer() missing 1 required positional argument: 'msg'




#########################################################################
# def print_msg(msg):
#     def printer(msg):
#         print(msg)
#     return printer
# print_msg("Hello")
#no output





#########################################################################
# def outer(a1):
#     def inner(a2):
#         print(a1 + a2)
#     return inner
# obj = outer(12)
# obj(15)
#27




#########################################################################
# def outer(a1):
#     def inner(a2):
#         print(a1 + a2)
#     return inner
# print(outer(10))
#<function outer.<locals>.inner at 0x036E9D68>



#########################################################################
# def outer(a1):
#     def inner(a2):
#         print(a1 + a2)
#     return inner
# obj = outer(10)
# print(obj(5))
# 15
# None



#########################################################################
# def outer(a1):
#     def inner(a2):
#         print(a1 + a2)
#     return inner
# obj = outer(10)
# print(obj(5))
# 15
# None




#########################################################################
# def outer(a1):
#     def inner(a2):
#         print(a1 + a2)
#     return inner()
# obj = outer(10)
# print(obj(5))
#TypeError: inner() missing 1 required positional argument: 'a2'




#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer()
# obj = print_msg("Hello")
#Hello


#########################################################################
# # def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer
# obj = print_msg("Hello")
# #No output



#########################################################################
# def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     return printer  # this got changed
# another = print_msg("Hello")
# #no output



#########################################################################
# def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     return printer()  # this got changed
# another = print_msg("Hello")
#Hello



#########################################################################
# def print_msg(msg):
# # This is the outer enclosing function
#     def printer():
# # This is the nested function
#         print(msg)
#     printer()
# # We execute the function
# # Output: Hello
# print_msg("Hello")
#Hello
#We can see that the nested function printer() was able to access the non-local variable msg of the enclosing function.




#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer()
# print_msg("aaa")
#aaa



#########################################################################=
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer
# print_msg("aaa")
#no output




#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer
# obj = print_msg("aaa")
#no output




#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer
# obj = print_msg("aaa")
# print(obj("aac"))
#TypeError: printer() takes 0 positional arguments but 1 was given





#########################################################################
#Defining a Closure Function
#def print_msg(msg):
# This is the outer enclosing function

#    def printer():
# This is the nested function
#        print(msg)

#    return printer  # this got changed
# Now let's try calling this function.
# Output: Hello
#another = print_msg("Hello")
#another()
#The print_msg() function was called with the string "Hello" 
#and the returned function was bound to the name another.
#On calling another(), the message was still remembered although 
#we had already finished executing the print_msg() function.
#This technique by which some data ("Hello") gets attached to the code is called closure in Python.



#########################################################################
# def print_msg(msg):
# # This is the outer enclosing function
#
#     def printer():
# # This is the nested function
#         print(msg)
#
#     return printer()  # this got changed
# # Now let's try calling this function.
# # Output: Hello
# another = print_msg("Hello")



#########################################################################
#def print_msg(msg):
#
#     def printer():
#         print(msg)
#
#     return printer
#
# another = print_msg("Hello")
# another()
# Hello






#########################################################################
# def print_msg(msg):
#     def printer():
#         print(msg)
#     return printer()
# another = print_msg("Hello")
#Hello




#########################################################################
# x = 'global'
# def outer_func():
#   y = 'enclose'
#   def inner_func():
#     z = 'local'
#     print(x, y, z)
#   inner_func()
# print(outer_func())
#global enclose local
#None




#########################################################################
# x = 'global'
# def outer_func():
#   y = 'enclose'
#   def inner_func():
#     z = 'local'
#     print(x, y, z)
#     def aaa():
#         print(z)
#     return  aaa()
#   return inner_func()
# print(outer_func())
# global enclose local
# local
# None



#########################################################################
#x = 'global'
# def outer_func():
#   y = 'enclose'
#
#   def inner_func():
#     z = 'local'
#     print(x, y, z)
#
#     def aaa():
#         print(z)
#     return  aaa
#
#   return inner_func()
#
# print(outer_func())
# global enclose local
# <function outer_func.<locals>.inner_func.<locals>.aaa at 0x04D89D60>





#########################################################################
# x = 'global'
# def outer_func():
#   y = 'enclose'
#   def inner_func():
#     z = 'local'
#     print(x, y, z)
#   inner_func()
# outer_func()
# print(outer_func())
#global enclose local
#global enclose local
#None




#########################################################################
# x = 'global'
# def outer_func():
#   y = 'enclose'
#   def inner_func():
#     z = 'local'
#     print(x, y, z)
#   inner_func()
# print(outer_func())
# global enclose local
# None




#########################################################################
# def outer_func():
#   x = 5
#   def inner_func(y = 3):
#     return (x + y)
#   return inner_func
# a = outer_func()
# print(a)	# 8





#########################################################################
# def outer_func():
#   x = 5
#   def inner_func(y = 3):
#     return (x + y)
#   return inner_func()
# print(outer_func())
#8



#########################################################################
# def outer_func():
#   x = 5
#   def inner_func(y = 3):
#     return (x + y)
#   return inner_func()
# print(outer_func())
# a = outer_func()
# print(a)
#8
#8



#########################################################################
# def outer_func():
#   x = 5
#   def inner_func(y = 3):
#     return (x + y)
#   return inner_func()
# print(outer_func())
# a = outer_func()
#8




#########################################################################
# def multiply_by(num):
#   def multiply_by_num(k):
#     return num * k
#   return multiply_by_num
# five = multiply_by(5)
# print(five(2))	# 10
# print(five(4))	# 20
# decimal = multiply_by(10)
# print(decimal(20))	# 200
# print(decimal(3))	# 30



