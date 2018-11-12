#closure.py
=====================
#Before getting into what a closure is, we have to first understand what a nested function and nonlocal variable is.
#A function defined inside another function is called a nested function. 
#Nested functions can access variables of the enclosing scope.
#In Python, these non-local variables are read only by default and 
#we must declare them explicitly as non-local (using nonlocal keyword) in order to modify them
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












