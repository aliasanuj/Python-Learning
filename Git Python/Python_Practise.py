#Python practise
#Simple Python Programs

#Python Program to Calculate the Average of Numbers in a Given List
n = int(input("Enter the no of elements ion list :"))
list1 = []
for i in range(0,n):
  m = int(input("enter element %s: "%i))
  list1.append(m)
avg = sum(list1)/n
print(avg)

n = int(input("Enter the no of elements ion list :"))
list1 = []
for i in range(0,n):
  m = int(input("enter element {}:".format(i)))
  list1.append(m)
avg = sum(list1)/n
print(avg)

#Python Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a=int(input("Enter value of first variable: "))
b=int(input("Enter value of second variable: "))
a=a+b
b=a-b
a=a-b
print("a is:",a," b is:",b)

#Python Program to Read a Mumber n and Compute n+nn+nnn
n=int(input("Enter a number n: "))
temp=str(n)
t1=temp+temp
t2=temp+temp+temp
comp=n+int(t1)+int(t2)
print("The value is:",comp)

n=int(input("Enter a number n: "))
n1 = n*n
n2 = n*n*n
final = n + n1 + n2
print(final)

#Python Program to Reverse a Given Number
n1 = int(input("Enter the number :"))
n2 = 0
while(n1>0):
  n3 = n1 % 10
  n2 = n2 * 10 + n3
  n1 = n1//10
print(n2)

#Python Program to Check Whether a Number is Positive or Negative
n=int(input("Enter number: "))
if(n>0):
    print("Number is positive")
else:
    print("Number is negative")

	
#Python Program to Take in the Marks of 5 Subjects and Display the Grade
sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub4)/5
if(avg>=90):
    print("Grade: A")
elif(avg>=80&avg<90):
    print("Grade: B")
elif(avg>=70&avg<80):
    print("Grade: C")
elif(avg>=60&avg<70):
    print("Grade: D")
else:
    print("Grade: F")

#Python Program to Print all Numbers in a Range Divisible by a Given Number
num1 = int(input("enter the 1st number : "))
num2 = int(input("enter the 2nd number : "))
num3 = int(input("Enter the number : "))
for i in range(num1,num2-1):
  if i%num3 == 0:
    print(i) 
#Python Program to Read Two Numbers and Print Their Quotient and Remainder
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
quotient=a//b
remainder=a%b
print("Quotient is:",quotient)
print("Remainder is:",remainder)

#Python Program to Accept Three Digits and Print all Possible Combinations from the Digits
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
d=[]
d.append(a)
d.append(b)
d.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if(i!=j&j!=k&k!=i):
                print(d[i],d[j],d[k])

#Python Program to Print Odd Numbers Within a Given Range
lower=int(input("Enter the lower limit for the range:"))
upper=int(input("Enter the upper limit for the range:"))
for i in range(lower,upper+1):
    if(i%2!=0):
        print(i)

#Python Program to Find the Sum of Digits in a Number
n1 = int(input("enter tye number - "))
n2 = 0
while(n1>0):
  n3 = n1 % 10
  n2 = n2 + n3
  n1 = n1//10
print(n2)

#group of numbers to list conversion
n1 = int(input("enter tye number - "))
n2 = map(int,str(n1))
print(list(n2))

n1 = int(input("enter tye number - "))
n2 = map(int,str(n1))
print(sum(list(n2)))

#Python Program to Find the Smallest Divisor of an Integer
x = int(input("enter the number - "))
list1 = []

for i in range(2,x+1):
  if x%i == 0:
    list1.append(i)
list1.sort()
print(list1[0])

#Python Program to Count the Number of Digits in a Number
n1 = int(input("enter the number - "))
n2 = map(int,str(n1))
print(len(list(n2)))

n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)

#Python Program to Check if a Number is a Palindrome
n1 = int(input("enter the humber : "))
n2 = 0
n3 = n1

while(n1>0):
  n4 = n1%10
  n2 = n2*10 + n4
  n1 = n1//10
if (n2==n3):
  print("this is palindrome")
else:
  print("not palindrome")


#Python Program to Print all Integers that Aren’t Divisible by Either 2 or 3 and Lie between 1 and 50.
for i in range(0,51):
    if(i%2 != 0 & i%3 != 0):
        print(i)

#Python Program to Read a Number n And Print the Series “1+2+…..+n= “

n1 = int(input("enter the number : "))
list1 = []
for i in range(1,n1+1):
  print(i,sep =" ",end =" ")
  if(i<n1):
    print("+",sep =" ",end =" ")
    list1.append(i)
print("=",sum(list1))

#Python Program to Read a Number n and Print the Natural Numbers Summation Pattern
n=int(input("Enter a number: "))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep=" ",end=" ")
        if(i<j):
            print("+",sep=" ",end=" ")
        a.append(i)
    print("=",sum(a))
 
Enter a number:  4
1 = 1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10

#Python Program to Print an Identity Matrix

n=int(input("Enter a number: "))
for i in range(0,n):
    for j in range(0,n):
        if(i==j):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

Enter a number:  4
1 0 0 0 
0 1 0 0 
0 0 1 0 
0 0 0 1 

##########################################
#list operations########################
##########################################

#Python Program to Find the Largest Number in a List
n1 = int(input("enter the elements : "))
n2 = []
for i in range(1,n1+1):
  n3 = int(input("enter the element {} :".format(i)))
  n2.append(n3)
n2.sort()
print(n2[-1])

#Python Program to Find the Second Largest Number in a List
n1 = int(input("enter the elements : "))
n2 = []
for i in range(1,n1+1):
  n3 = int(input("enter the element {} :".format(i)))
  n2.append(n3)
n2.sort()
print(n2)
print(n2[-2])

#Python Program to Put Even and Odd elements in a List into Two Different Lists
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
even=[]
odd=[]
for j in a:
    if(j%2==0):
        even.append(j)
    else:
        odd.append(j)
print("The even list",even)
print("The odd list",odd)

#Python Program to Merge Two Lists and Sort it
a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)


#Python Program to Sort a List According to the Length of the Elements
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=input("Enter element:")
    a.append(b)
a.sort(key=len)
print(a)

#union | interswct | unique
def unique(a):
    """ return the list with duplicate elements removed """
    return list(set(a))

def intersect(a, b):
    """ return the intersection of two lists """
    return list(set(a) & set(b))

def union(a, b):
    """ return the union of two lists """
    return list(set(a) | set(b))

if __name__ == "__main__": 
    a = [0,1,2,0,1,2,3,4,5,6,7,8,9]
    b = [5,6,7,8,9,10,11,12,13,14]
    print(unique(a))
    print(intersect(a, b))
    print(union(a, b))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

#Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
n1 = int(input("enter the number -"))
n2 = int(input("enter the number -"))
n3 = [(x,x**2) for x in range(n1,n2)]
print(n3)

enter the number - 1
enter the number - 5
[(1, 1), (2, 4), (3, 9), (4, 16)]

#to take eny number and make the sum of that numberx = 15
x = 15
print(sum(list(map(int,str(x)))))
#output --> 6

#Python Program to Find all Numbers in a Range which are Perfect Squares and Sum of all Digits in the Number is Less than 10
l=int(input("Enter lower range: "))
u=int(input("Enter upper range: "))
a=[]
a=[x for x in range(l,u+1) if (int(x**0.5))**2==x and sum(list(map(int,str(x))))<10]
print(a)

#Python Program to Find the Cumulative Sum of a List where the ith Element is the Sum of the First i+1 Elements From The Original List
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The original list is: ",a)
print("The new list is: ",b)

Enter the number of elements in list: 5
Enter element1: 1
Enter element2: 2
Enter element3: 6
Enter element4: 5
Enter element5: 4
The original list is:  [1, 2, 6, 5, 4]
The new list is:  [1, 3, 9, 14, 18]

import itertools
list1 = [1,2,3,4,5,6]
print(list(itertools.accumulate(list1)))
[1, 3, 6, 10, 15, 21]

#Python Program to Generate Random Numbers from 1 to 20 and Append Them to the List
import random
a=[]
n=int(input("Enter number of elements:"))
for j in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)

#Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
def last(n):
    return n[-1]  
 
def sort(tuples):
    return sorted(tuples, key=last)
 
a=input("Enter a list of tuples:")
print("Sorted:")
print(sort(a))

Case 1:
Enter a list of tuples:[(2,5),(1,2),(4,4),(2,3)]
Sorted:
[(1, 2), (2, 3), (4, 4), (2, 5)]
 
Case 2:
Enter a list of tuples:[(23,45),(25,44),(89,40)]
Sorted:
[(89, 40), (25, 44), (23, 45)]

#Python Program to Swap the First and Last Value of a List
a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)

Enter the number of elements in list: 5
Enter element1: 1
Enter element2: 4
Enter element3: 7
Enter element4: 8
Enter element5: 9
New list is:
[9, 4, 7, 8, 1]

#Python Program to Remove the Duplicate Items from a List
list1 = [1,47,59,78,2,3,6,5,4,7,8,9,6,3]
print(set(list1))
print(list(set(list1)))

{1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 47, 59}
[1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 47, 59]

#Python Program to Read a List of Words and Return the Length of the Longest One
list1 = ["anuj","chetaN"]
list2 = []
for i in list1:
  x = len(i)
  list2.append(x)
print(list2)


list1 = ["anuj","anhshjds","chetaN"]
x = max(list1, key = len)
print(x)

list1 = ["anuj","anhshjds","chetaN"]
x = min(list1, key = len)
print(x)


##########################################
#String operations########################
##########################################

#Python Program to Replace all Occurrences of ‘a’ with $ in a String
string=str(input(("Enter string:")))
string=string.replace('a','$')
string=string.replace('A','$')
print("Modified string:")
print(string)

#Python Program to Remove the nth Index Character from a Non-Empty String
def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=str(input(("Enter the sring:")))
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))

Enter the sring: aanuja
Enter the index of the character to remove: 1
Modified string:
anuja

#Python Program to Detect if Two Strings are Anagrams
a1 = "kumaranuj"
a2 = "anujkumar"
b1 = sorted(a1)
print(b1)
b2 = sorted(a2)
print(b2)

['a', 'a', 'j', 'k', 'm', 'n', 'r', 'u', 'u']
['a', 'a', 'j', 'k', 'm', 'n', 'r', 'u', 'u']

s1=raw_input("Enter first string:")
s2=raw_input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")
	  
#Python Program to Form a New String where the First Character and the Last Character have been Exchanged
def change(string):
      return string[-1:] + string[1:-1] + string[:1]
string=str(input(("Enter string:")))
print("Modified string:")
print(change(string))

Enter string: kumar anuj
Modified string:
jumar anuk

#Python Program to Count the Number of Vowels in a String
string=str(input("Enter string:"))
vowels=0
for i in string:
      if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
print("Number of vowels are:")
print(vowels)


n1 = str(input("enter the string :"))
n2 = []
v = ["a","e","i","o","u"]
for i in n1:
  if i in v:
    n2.append(i)
print("vowels are ",len(n2))


#Python Program to Take in a String and Replace Every Blank Space with Hyphen
n1 = str(input("enter the string :"))
x = n1.replace(" ","-")
print(x)

enter the string : my name is kumar anuj
my-name-is-kumar-anuj

#Python Program to Calculate the Length of a String Without Using a Library Function
string=str(input(("Enter string:")))
count=0
for i in string:
      count=count+1
print("Length of the string is:")
print(count)

#conversion sentance --> list --> sentances
n1 = str(input("Enter the sentence : "))
n2 = n1.split()
print(n2)
n3 = " ".join(n2)
print(n3)

Enter the sentence :  kumar anuj
['kumar', 'anuj']
kumar anuj

#Python Program to Remove the Characters of Odd Index Values in a String
def modify(string):  
  final = ""   
  for i in range(len(string)):  
    if i % 2 == 0:  
      final = final + string[i]  
  return final
string=str(input("Enter string:"))
print("Modified string is:")
print(modify(string))

Enter string: kumaranuj
Modified string is:
kmrnj

#Python Program to Calculate the Number of Words and the Number of Characters Present in a String
string=raw_input("Enter string:")
char=0
word=1
for i in string:
      char=char+1
      if(i==' '):
            word=word+1
print("Number of words in the string:")
print(word)
print("Number of characters in the string:")
print(char)

#larger string | smaller string
string1=str(input("Enter first string:"))
string2=str(input("Enter second string:"))
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)

Enter first string: kumar
Enter second string: anuj
Larger string is:
kumar

#Python Program to Count Number of Lowercase Characters in a String
string=str(input("Enter string:"))
count=0
for i in string:
      if(i.islower()):
            count=count+1
print("The number of lowercase characters is:")
print(count)

#Python Program to Count Number of Uppercase Characters in a String
string=str(input("Enter string:"))
count=0
for i in string:
      if(i.isupper()):
            count=count+1
print("The number of lowercase characters is:")
print(count)


#Python Program to Check if a String is a Palindrome or Not
string=str(input("Enter string:"))
if(string==string[::-1]):
      print("The string is a palindrome")
else:
      print("The string isn't a palindrome")

	  
#Python Program to Calculate the Number of Upper Case Letters and Lower Case Letters in a String
string=str(input("Enter string:"))
count1=0
count2=0
for i in string:
      if(i.islower()):
            count1=count1+1
      elif(i.isupper()):
            count2=count2+1
print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)


#Python Program to Calculate the Number of Digits and Letters in a String
string=str(input("Enter string:"))
count1=0
count2=0
for i in string:
      if(i.isdigit()):
            count1=count1+1
      count2=count2+1
print("The number of digits is:")
print(count1)
print("The number of characters is:")
print(count2)


#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String=str(input("Enter string:"))
count=0
for i in string:
      count=count+1
new=string[0:2]+string[count-2:count]
print("Newly formed string is:")
print(new)


#Python Program to Count the Occurrences of Each Word in a Given String Sentence
n1=str(input("Enter string:"))
n2 = []
n3 = str(input("Enter string:"))
count=0
n2 = n1.split(" ")

for i in range(0,len(n2)):
  if n3 == n2[i]:
    count = count + 1
print(count)


#Python Program to Check if a Substring is Present in a Given String
string=str(input("Enter string:"))
sub_str=str(input("Enter word:"))
if(string.find(sub_str)==-1):
      print("Substring not found in string!")
else:
      print("Substring in string!")
	  
string=str(input("Enter string:"))
sub_str=str(input("Enter word:"))
for i in range(0,len(string)):
  if sub_str in string:
    print("it is there")
    break
  else:
    print("not there")
    break
	
##########################################
#dictionary operations########################
##########################################

#Python Program to Add a Key-Value Pair to the Dictionary
key=int(input("Enter the key (int) to be added:"))
value=int(input("Enter the value for the key to be added:"))
d={}
d.update({key:value})
print("Updated dictionary is:")
print(d)

#Python Program to Concatenate Two Dictionaries Into One
d1={'A':1,'B':2}
d2={'C':3}
d1.update(d2)
print("Concatenated dictionary is:")
print(d1)

#Python Program to Check if a Given Key Exists in a Dictionary or Not
d={'A':1,'B':2,'C':3}
key=str(input("Enter key to check:"))
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")  ##case sensitive 
	  

	  
#Python Program to Generate a Dictionary that Contains Numbers (between 1 and n) in the Form (x,x*x).
n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)

#Python Program to Sum All the Items in a Dictionary
d={'A':100,'B':540,'C':239}
print("Total sum of values in the dictionary:")
print(sum(d.values()))
print(d.values())



