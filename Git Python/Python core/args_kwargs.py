#args_kwargs.py
=======================
def myFun(*argv):  
    for arg in argv:  
        print (arg) 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
#Hello
#Welcome
#to
#GeeksforGeeks
============================
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg)
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')
#First argument : Hello
#Next argument through *argv : Welcome
#Next argument through *argv : to
#Next argument through *argv : GeeksforGeeks
============================
def myFun(**kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
myFun(first ='Geeks', mid ='for', last='Geeks')
#first == Geeks
#mid == for
#last == Geeks
=============================
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')     
#first == Geeks
#mid == for
#last == Geeks
=============================
def myFun(arg1, arg2, arg3): 
    print("arg1:", arg1) 
    print("arg2:", arg2) 
    print("arg3:", arg3) 
# Now we can use *args or **kwargs to 
# pass arguments to this function :  
args = ("Geeks", "for", "Geeks") 
myFun(*args) 
kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"} 
myFun(**kwargs) 
#arg1: Geeks
#arg2: for
#arg3: Geeks
#arg1: Geeks
#arg2: for
#arg3: Geeks
==============================
def adder(*num):
    sum = 0
    for n in num:
        sum = sum + n
    print("Sum:",sum)
adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)
#Sum: 8
#Sum: 22
#Sum: 17
==============================
def intro(**data):
    print("\nData type of argument:",type(data))
    for key, value in data.items():
        print("{} is {}".format(key,value))
intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Age=25, Phone=9876543210)
#Data type of argument: <class 'dict'>
#Firstname is Sita
#Lastname is Sharma
#Age is 22
#Phone is 1234567890

#Data type of argument: <class 'dict'>
#Firstname is John
#Lastname is Wood
#Email is johnwood@nomail.com
#Country is Wakanda
#Age is 25
#Phone is 9876543210
===================================
def test_var_args(f_arg, *argv):
    print ("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv :", arg)
test_var_args('yasoob','python','eggs','test')
#first normal arg: yasoob
#another arg through *argv : python
#another arg through *argv : eggs
#another arg through *argv : test
====================================
def test_var_args(farg, *args):
    print ("formal arg:", farg)
    for arg in args:
        print ("another arg:", arg)
test_var_args(1, "two", 3)
#formal arg: 1
#another arg: two
#another arg: 3
====================================
def find_avg(*numbers):
  sum = 0
  for i in numbers :
    sum += i
  print ("average is ",sum/(len(numbers)))
  print (numbers)
find_avg(2,3)
find_avg(2,3,4)
find_avg(1,2,3,4,5,6,7,8,9,10)
#average is  2.5
#(2, 3)
#average is  3.0
#(2, 3, 4)
#average is  5.5
#(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
====================================
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key in kwargs:
        print("another keyword arg: %s: %s" % (key, kwargs[key]))
test_var_kwargs(farg=1, myarg2="two", myarg3=3)
#formal arg: 1
#another keyword arg: myarg2: two
#another keyword arg: myarg3: 3
==========================
def test_var_args_call(arg1, arg2, arg3):
    print ("arg1:", arg1)
    print ("arg2:", arg2)
    print ("arg3:", arg3)
kwargs = {"arg3": 3, "arg2": "two"}
test_var_args_call(1, **kwargs)
#arg1: 1
#arg2: two
#arg3: 3
===========================
def abc(**data):
  for x,y in data.items():
    print("{} is {}".format(x,y))
abc(name="anuj",city="patna")
abc(name="aman",city="agra",rollno=101,company="NIIT")
#name is anuj
#city is patna
#name is aman
#city is agra
#rollno is 101
#company is NIIT
==================================
