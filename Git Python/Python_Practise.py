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

#String operations

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

