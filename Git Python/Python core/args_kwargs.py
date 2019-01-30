#args_kwargs.py
==================================
1. Args --> The special syntax "*" is function in python is used to pass variable number of arguments to a function.
2. It is used to pass non-keyworded variable-length argument list.
3. The syntax is used to symbol * to take in variable numbers of arguments,by convention it is often used with the word args.
* args allows us to do is take an in more aeguments than the number of formal of arguments that you previously defined.
with * args,any number of extra arguments can be tracked on to your current formal parameter.
================================
1. kwargs : The special syntax **kwargs in function definations in python is used to pass a keyword, variable-length argument list.
2. We use the name kwargs with double star. The reason is because the double star allow us to pass through keyword arguments(and any number)
3. A key word argument is where you provide a name to the variable as you pass into function.
=======================================
def abc(a, *b, **c):
    print("first argument is ",a)
    for i in b:
        print(i, end = " ")
    print("\n")
    for j in c.items():
        print(j)
abc("anuj", "kumar", "dfvdf", one = "dbvfdfj", two="vknjd" , three="fklnhdf")
#first argument is  anuj
#kumar dfvdf 
#('one', 'dbvfdfj')
#('two', 'vknjd')
#('three', 'fklnhdf')
=======================================
def abc(a, *b, **c):
    print("first argument is ",a)
    for i in b:
        print(i, end = " ")
    print("\n")
    for j in c.items():
        print(j)
list1 = ["ckvnd","dvjdf","bmngfjbn"]
abc(list1, "kumar", "dfvdf", one = "dbvfdfj", two="vknjd" , three="fklnhdf")
#first argument is  ['ckvnd', 'dvjdf', 'bmngfjbn']
#kumar dfvdf 
#('one', 'dbvfdfj')
#('two', 'vknjd')
#('three', 'fklnhdf')
========================================
def myFun(**kwargs):
    for i in kwargs.values():
        print(i)
myFun(first ='Geeks', mid ='for', last='Geeks')

#Geeks
#for
#Geeks
====================================
def myFun(**kwargs):
    for i in kwargs.items():
        print(i)
myFun(a=10, b=20,c=30)
myFun(a="10", b="20",c="30")
#myFun("a"="10", "b"="20","c"="30") #SyntaxError: keyword can't be an expression
#myFun(1="10", 2="20",3="30") #SyntaxError: keyword can't be an expression

#('a', 10)
#('b', 20)
#('c', 30)
#('a', '10')
#('b', '20')
#('c', '30')
===================================
def myFun(**kwargs):
    for i in kwargs.items():
        print(i)
myFun(first ='Geeks', mid ='for', last='Geeks')

#('first', 'Geeks')
#('mid', 'for')
#('last', 'Geeks')
================================
def myFun(**kwargs):
    for i in kwargs.items():
        print(i)
myFun(a='Geeks',b='for',c='Geeks')

#('a', 'Geeks')
#('b', 'for')
#('c', 'Geeks')
===============================
def myFun(**kwargs):
    for i in kwargs.items():
        print(i)
myFun('Geeks','for','Geeks')
#error TypeError: myFun() takes 0 positional arguments but 3 were given
================================
def myFun(**kwargs):
    for i in kwargs.items():
        print(i)
myFun(1=10,2=15,3=20)
#SyntaxError: keyword can't be an expression
==============================
def myFun(**kwargs):
    for i in kwargs.items():
        print("%s = %s"%(i))
myFun(first ='Geeks', mid ='for', last='Geeks')

#first = Geeks
#mid = for
#last = Geeks
===============================
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for i in kwargs.items():
        print("{}".format(i))
test_var_kwargs(farg=1, myarg2="two", myarg3=3)

#formal arg: 1
#('myarg2', 'two')
#('myarg3', 3)
==============================
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for i in kwargs.items():
        print(i)
test_var_kwargs(farg=1, myarg2="two", myarg3=3)

#formal arg: 1
#('myarg2', 'two')
#('myarg3', 3)
===============================

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
def myFun(arg1, *argv,**abc):
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
============================
def myFun(**argv):  
    for arg in argv:  
        print (arg) 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks') 
#TypeError: myFun() takes 0 positional arguments but 4 were given
============================
def myFun(**kwargs):  
    for i in kwargs.items(): 
        print (i) 
myFun(first ='Geeks', mid ='for', last='Geeks')
#('first', 'Geeks')
#('mid', 'for')
#('last', 'Geeks')
=================================
def myFun(arg,**kwargs):  
    print(arg)
    for i in kwargs.items(): 
        print (i) 
myFun('anuj',first ='Geeks', mid ='for', last='Geeks')

#anuj
#('first', 'Geeks')
#('mid', 'for')
#('last', 'Geeks')
   
==================================
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks')     
#first == Geeks
#mid == for
#last == Geeks
=======================================
def myFun(arg1, **kwargs):  
    for key,value in kwargs.items(): 
        print ("{} and {}".format(key,value)) 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 
#first and Geeks
#mid and for
#last and Geeks
==================================================
def myFun(arg1, **kwargs):  
  print("the first arg is : ",arg1)
  for key,value in kwargs.items(): 
    print ("{} and {}".format(key,value)) 
myFun("Hi", first ='Geeks', mid ='for', last='Geeks') 
#the first arg is :  Hi
#first and Geeks
#mid and for
#last and Geeks
==============================================
def test_var_kwargs(farg, **kwargs):
    print("formal arg:", farg)
    for key,value in kwargs.items():
        print("{} and {} ".format(key, value))
test_var_kwargs(farg=1, myarg2="two", myarg3=3)
#formal arg: 1
#myarg2 and two 
#myarg3 and 3
===============================================
def test_var_kwargs(farg, *kwargs):
    print("formal arg:", farg)
    for i in kwargs.items():
        print(i)
test_var_kwargs(farg=1, myarg2="two", myarg3=3)
#TypeError: test_var_kwargs() got an unexpected keyword argument 'myarg2'

===============================================
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
def abc(a,*b):
    print("the first parameter is ",a)
    for i in (b):
        print("the second paameter is ",i)
abc("anuj","aman","anshu","chetan")
#the first parameter is  anuj
#the second paameter is  aman
#the second paameter is  anshu
#the second paameter is  chetan
=============================================
def abc(a,**b):
    print("the first parameter is ",a)
    for i in (b):
        print("the second paameter is ",i)
abc(a="anuj",b="aman",c="anshu",d="chetan")
#the first parameter is  anuj
#the second paameter is  b
#the second paameter is  c
#the second paameter is  d
===========================================
