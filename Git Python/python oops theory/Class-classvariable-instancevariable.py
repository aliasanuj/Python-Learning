=================================
=============================
===========Class=============
=============================

1. A Class is like an object constructor, or a "blueprint" for creating objects.
2. To create a class, use the keyword class.
3. Classes provide a means of bundling data and functionality together
4. Creating a new class creates a new type of object, allowing new instances of that type to be made.
5. A class is a code template for creating objects.
6. Objects have member variables and have behaviour associated with them.

==================================
======Instance variable===========
==================================

1. Instance variables are owned by instances of the class. This means that for each object or instance of 
a class, the instance variables are different.
2. Unlike class variables, instance variables are defined within methods.
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
When we create a Shark object, we will have to define these variables, which are passed as parameters 
within the constructor method or another method.
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
new_shark = Shark("Sammy", 5)
=================================
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("aa")
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(age)
new_shark = Shark("Sammy", 5)
#5
=================================
class Shark:
    def __init__(self, name, age):
        self.anything = name
        self.anything = age
        print(name)
new_shark = Shark("Sammy", 5)
#5
=================================
class Shark:
    def __init__(self, name, age):
        self.name = "aaa"
        self.age = 58
        print("aa")
class Shark:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(age)
new_shark = Shark("Sammy", 5)
#5
=================================good example
=================================
class Shark:
    def __init__(self, name, age):
        self.name = "aaa"
        self.age = 58
        print("aa")
    def __init__(self, name, age):
        self.name = "anuj"
        self.age = age
        print(name)
        print(self.name)
new_shark = Shark("Sammy", 5)
#Sammy
#anuj
=================================
3. Instance variables, owned by objects of the class, allow for each object or instance to have different 
values assigned to those variables.
=====================================
=======Class variable================
=====================================

1. Class variables are defined within the class construction. Because they are owned by the class itself, 
class variables are shared by all instances of the class. They therefore will generally have the same value 
for every instance unless you are using the class variable to initialize a variable.
2. Defined outside of all the methods, class variables are, by convention, typically 
placed right below the class header and before the constructor method and other methods.
=================================
class Shark:
    animal_type = "fish"
=================================
class Shark:
    animal_type = "fish"
    location = "ocean"
    followers = 5
new_shark = Shark()
print(new_shark.animal_type)
print(new_shark.location)
print(new_shark.followers)
#fish
#ocean
#5

Working with Class and Instance Variables Together:
===================================================
class Shark:
  # Class variables
    animal_type = "fish"
    location = "ocean"
  # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
  # Method with instance variable followers
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")
def main():
    # First object, set up instance variables of constructor method
    sammy = Shark("Sammy", 5)
    # Print out instance variable name
    print(sammy.name)
    # Print out class variable location
    print(sammy.location)
    # Second object
    stevie = Shark("Stevie", 8)
    # Print out instance variable name
    print(stevie.name)
    # Use set_followers method and pass followers instance variable
    stevie.set_followers(77)
    # Print out class variable animal_type
    print(stevie.animal_type)
main()

#Sammy
#ocean
#Stevie
#This user has 77 followers
#fish
==============================
class Shark:
    animal_type = "fish"
    location = "ocean"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def set_followers(self, followers):
        print("This user has " + str(followers) + " followers")
def main():
    sammy = Shark("Sammy", 5)
    print(sammy.name)
    print(sammy.location)
    stevie = Shark("Stevie", 8)
    print(stevie.name)
    stevie.set_followers(77)
    print(stevie.animal_type)
    print(sammy.animal_type)
main()

#Sammy
#ocean
#Stevie
#This user has 77 followers
#fish
#fish
==============================
class abc():
    a = "anuj"
    b = "ball"
    def inner(self):
        c = "cat"
        print("inner")
    d = "dog"
obj1 = abc()
print(obj1.a)
print(obj1.b)
print(obj1.d)
obj1.inner()
#anuj
#ball
#dog
#inner
========================================GE
========================================
class abc():
    a = "anuj"
    b = "ball"
    def inner(self):
        c = "cat"
        print("inner")
    d = "dog"
obj1 = abc()
print(obj1.a)
print(obj1.b)
#print(obj1.c) #error
obj1.inner()
#anuj
#ball
#inner
========================================
==class vs instance variable============
========================================
1. At the class level, variables are referred to as class variables, whereas variables at the instance 
level are called instance variables.
2. Instance variables are for data which is unique to every object but, Class variables are for data 
shared between different instances of a class.
==> Class or static variables are shared by all objects.
==>Instance or non-static variables are different for different objects (every object has a copy of it)
