#closure.py
=====================
#Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.
#A function defined inside another function is called a nested function. 
#Nested functions can access variables of the enclosing scope.
#In Python, these non-local variables are read only by default and 
#we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them
#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory. 
=====================================
# base concept of decoorator is closore
def gen_multiplier(x):
    def multiplier(y):
        return x * y
    return multiplier
obj = gen_multiplier(10)
print(obj(5))
#50
=======================
def gen_multiplier():
    x = 10 #non-local variable
    def multiplier(y): #stores the reference to non-local variable
        return x * y #x is non local to multiplier
    return multiplier
#call the function
obj = gen_multiplier()
del gen_multiplier #it will delete
print(obj(5))

#50
==========================
#nested-function
#nested function should access non-local variable
#it should return the en-closed function
=====================================
def print_msg(msg):
# This is the outer enclosing function
    def printer():
# This is the nested function
        print(msg)
    printer()
# We execute the function
# Output: Hello
print_msg("Hello")

#Hello
#We can see that the nested function printer() was able to access the non-local variable msg of the enclosing function.
=================================
#Defining a Closure Function

def print_msg(msg):
# This is the outer enclosing function

    def printer():
# This is the nested function
        print(msg)

    return printer  # this got changed

# Now let's try calling this function.
# Output: Hello
another = print_msg("Hello")
another()

#The print_msg() function was called with the string "Hello" 
#and the returned function was bound to the name another.
#On calling another(), the message was still remembered although 
#we had already finished executing the print_msg() function.
#This technique by which some data ("Hello") gets attached to the code is called closure in Python.
==================================================

x = 'global'
def outer_func():
  y = 'enclose'
  def inner_func():
    z = 'local'
    print(x, y, z)
  inner_func()
print(outer_func())

#global enclose local
#None
================================
def outer_func():
  x = 5
  def inner_func(y = 3):
    return (x + y)
  return inner_func
a = outer_func()
 
print(a())	# 8

=======================
def multiply_by(num):
  def multiply_by_num(k):
    return num * k
  return multiply_by_num
  
five = multiply_by(5)
print(five(2))	# 10
print(five(4))	# 20
 
decimal = multiply_by(10)
print(decimal(20))	# 200
print(decimal(3))	# 30
=========================












