#basic 

num1 = int(input("Enter how many numbers you want to add in list"))
blank_list = []

for i in range(0,num1):
  num2 = int(input("enter the number"))
  blank_list.append(num2)

print("the number which you have been entered",blank_list)

sumOfNumberInList = sum(blank_list)
print("sum of all numbers which you have entered - ",sumOfNumberInList) 

average = sumOfNumberInList/num1

print("the average of the numbers is - " ,average)



=======================================

def abc(list1):
  list2 = []
  for i in list1:
    if i not in list2:
      list2.append(i)
  return list2

list1 = ["one","two","three","one","two","three"]
print(abc(list1))


=====================================

string = "my nams is anuj"

stringToList = string.split()
reversedString = " ".join(reversed(stringToList))
print(reversedString.capitalize())




========================================


number1 = int(input("Enter the first number"))
number2 = int(input("Enter the second number"))

number1 = number1 + number2
number2 = number1 - number2
number1 = number1 - number2

print("number1 is ",number1," and number2 is ",number2)




================================================



number1 = int(input("enter any number"))
number2 = 0

while(number1>0):
  number3 = number1 % 10
  number2 = number2 * 10 + number3
  number1 = number1 // 10

print("the reversed number is ",number2)



====================================



number1 = int(input("wnter any number"))

if (number1 > 0):
  print("number is positive")
else:
  print("number is negative")



======================================

num1 = int(input("enter the starting number - "))
num2 = int(input("enter the ending number - "))
num3 = int(input("enter the divisble number - "))

for i in range(num1,num2+1):
  if (i%num3 == 0):
    print(i)








======================================



number1 = int(input("enter the number"))
number2 = int(input("enter the number which you want to divide"))

quotient = number1 // number2
reminder = number1 % number2

print("the quotient is ",quotient, "and reminder is ",reminder)



==============================

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))
num3 = int(input("enter 3rd number"))

d = []

d.append(num1)
d.append(num2)
d.append(num3)

for i in range(0,3):
  for j in range(0,3):
    for k in range(0,3):
      if (i!=j & j!=k & k!=i):
        print(d[i],d[j],d[k])

======================================


number1 = int(input("enter the first number"))
number2 = int(input("enter the second number"))

for i in range(number1, number2):
  if (i%2 == 0):
    print(i)




================================

number1 = int(input("enter any number"))
number2 = str(number1)
print(len(number2))


====================================


n = int(input("enter the number"))

count = 0
while(n>0):
  count = count + 1
  n = n//10

print(count)

=============================
number1 = int(input("enter the number"))
list1 = []
for i in range(0,number1+1):
  list1.append(i)

print(sum(list1))


=======================

number1 = int(input("enter the number - "))

list1 = []
list2 = []
list3 = []
list4 = []

for i in range(0,number1):
  number2 = int(input("element"))
  list1.append(number2)

print("list is - ",list1)

for i in list1:
  if i%2 == 0:
    list2.append(i)
print("sum of even number is ",sum(list2))

for i in list1:
  if i%2 != 0:
    list3.append(i)
print("sum of odd number is ",sum(list3))

for i in list1:
  if i<0:
    list4.append(i)
print("sum of negative number is ",sum(list4))


============================

number1 = int(input("enter the numbers of elements in list - "))
list1 = []
list2 = []
list3 = []

for i in range(0,number1):
  number2 = int(input("elements in list - "))
  list1.append(number2)

print("your list is - ",list1)

for i in list1:
  if i%2==0:
    list2.append(i)
print("biggest even number no is -",list2[-1])

for i in list1:
  if i%2!=0:
    list3.append(i)
print("biggest even number no is -",list3[-1])






===============================

number1 = int(input("enter the number"))
number2 = 0
number4 = number1

while(number1>0):
  number3 = number1 % 10
  number2 = number2 *10 + number3
  number1 = number1 // 10

if (number4 == number2):
  print("it is palindrome")
else:
  print("it is not palindrome")

====================================



num1 = int(input("enter the number of elements you want to add"))
list1 = []
list2 = []
list3 = []

for i in range(0,num1):
  num2 = int(input("elements - "))
  list1.append(num2)
print(list1)

for j in range(0,num1):
  num2 = int(input("elements - "))
  list2.append(num2)
print(list2)

c = list1+list2
c.sort()
print(c)

for x in c:
  if x not in list3:
    list3.append(x)

print(list3)

================================

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))

for i in range(num1,num2):
  num3 = i**2
  if (num3 <= num2):
    num4 = list(map(int,str(num3)))
    if sum(num4) < 10:
        print(int(''.join(map(str,num4))))


===================================
list1 = [5,2,3,4,5,6,7,8,9]
num1 = 0
num2 = []
for i in list1:
  num1 = num1 + i
  num2.append(num1)
print(num2)

===================================

list1 = [1,2,5,4,77,89,55,11,2,35,69,4,9,2]
num1 = list1[0]
num2 = list1[-1]

list1[0] = num2
list1[-1] = num1

print(list1)
=========================
num1 = int(input("enter the number of words you want gto enter"))
list1 = []
for i in range(1,num1+1):
  num2 = input("elements : ")
  length = len(num2)
  list1.append(length)

list1.sort()
print(list1[-1])


=============================


num1 = int(input("enter the number of words you want gto enter"))
list1 = []
for i in range(1,num1+1):
  num2 = input("elements : ")
  length = num2
  list1.append(length)

list1.sort()
print(list1[-1])


=================================

s1=str(input("Enter first string:"))
list1 = []
list2 = ['a','e','i','o','u']

for i in s1:
  for j in list2:
    if i == j:
      list1.append(i)
print(len(list1))

==============================

s1=str(input("Enter first string:"))

str2 = s1.replace(' ','-')
print(str2)

============================

s1=str(input("Enter first string:"))
count = 0
for i in s1:
  count = count + 1

print(count)

=====================

a = str(input("enter any words : "))
print(list(a))
list1 = []

list1.append(a[0])
list1.append(a[1])
list1.append(a[-2])
list1.append(a[-1])

x = "".join(map(str,list1))
print(x)
=============================
mydict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
for k, v in mydict.iteritems():
    if k == 'two':
        del mydict[k]

===============================
info = [{"eId":1001,"eName":"anuj", "eSalary":25000},
        {"eId":1002,"eName":"aman", "eSalary":26000},
        {"eId":1003,"eName":"anshu", "eSalary":27000}]

#to add a new employee
print(info)

empId = input("Enter the eId")
empName = input("Enter the name")
empSalary = input("Enter the salary")

def addNewEntry():
  info.append({"eId":empId, "eName":empName, "eSalary":empSalary})
  print(info)

addNewEntry()
======================================
info = [{"eId":1001,"eName":"anuj", "eSalary":25000},
        {"eId":1002,"eName":"aman", "eSalary":26000},
        {"eId":1003,"eName":"anshu", "eSalary":27000}]

#to add a new employee
print(info)

print("\n")

def sorting():
  sortingList = sorted(info , key = lambda k : k['eName'])
  print(sortingList)
sorting()
==============================================
info = [{"eId":1001,"eName":"anuj", "eSalary":27000},
        {"eId":1002,"eName":"aman", "eSalary":26000},
        {"eId":1003,"eName":"anshu", "eSalary":28000}]

#to add a new employee
print(info)

print("\n")

def sorting():
  sortingList = sorted(info , key = lambda k : k['eSalary'])
  print(sortingList)
sorting()
=======================================================
info = [{"eId":1001,"eName":"anuj", "eSalary":27000},
        {"eId":1002,"eName":"aman", "eSalary":26000},
        {"eId":1003,"eName":"anshu", "eSalary":28000}]

#to add a new employee
print(info)

print("\n")

def search():
    findName= input("Enter the name which you want to search: ")
    count = 0
    for ename in info:
        if(ename["eName"].lower() == findName.lower()):
            print("Details : {}".format(ename))
            count = count + 1
    if count ==0:
      print("no name found !! Try again. ")
search()


===============================================================


sentence = "The quick brown fox jumped over the lazy dog"

words = sentence.split()

print(words) #it will convert into list

sentence_rev = " ".join(reversed(words))

print (sentence_rev.capitalize())


========================================

string = "I am kumar anuj"
list1 = string.split()
print(list1)
reversed_list1 = " ".join(reversed(list1))
print(reversed_list1)
print(reversed_list1.capitalize())





=====================================
def finallist(list1):
  final_list = []
  for i in list1:
    if i not in final_list:
      final_list.append(i)
  return final_list

list1 = ["one","two","one","three","three","two"]
print(finallist(list1))
========================

list2 = [{"inf01":{"empID":1001, "empName":"anuj" ,"empSalary":2000},
         "info2":{"empID":1002, "empName":"satya" ,"empSalary":8000},
         "info3":{"empID":1003, "empName":"nitin" ,"empSalary":6000}} ]


# first of all, you should never overload a reserved word
# dict is a reserved word
# the best practice is to give meaningful names to variables

countries = {
    "ae" : {
        "name" : "united arab emirates",
        "status" : "n"
    },
    "at" : {
        "name" : "austria",
        "status" : "n"
    },
    "au" : {
        "name" : "australia",
        "status" : "n"
    }
}

def search():
    findName = input("Enter the name which you want to search: ")
    count = 0
    for key, item in countries.items():
        if item["name"].lower() == findName.lower():
            print("Details : {0} - {1}".format(key, item["name"]))
            count = count + 1
            if count == 0:
                print("no name found !! Try again. ")
                search()


if __name__ == '__main__':
    search()


countries = {
	"ae": {
		"name": "United Arab Emirates",
		"status": "n"
	},
	"at": {
		"name": "Austria",
		"status": "n"
	},
	"au": {
		"name": "Australia",
		"status": "n"
	},
	"be-fr": {
		"name": "Belgium (French)",
		"status": "n"
	},
	"be-nl": {
		"name": "Belgium (Dutch)",
		"status": "n"
	},
	"br": {
		"name": "Brazil",
		"status": "n"
	},
	"ca": {
		"name": "Canada (English)",
		"status": "n"
	},
	"ch-de": {
		"name": "Switzerland (German)",
		"status": "n"
	},
	"ch-fr": {
		"name": "Switzerland (French)",
		"status": "n"
	},
	"cn": {
		"name": "China",
		"status": "n"
	},
	"cz": {
		"name": "Czech Republic",
		"status": "n"
	},
	"de": {
		"name": "Germany",
		"status": "n"
	},
	"dk": {
		"name": "Denmark",
		"status": "n"
	},
	"es": {
		"name": "Spain",
		"status": "n"
	},
	"fi": {
		"name": "Finland",
		"status": "n"
	},
	"fr": {
		"name": "France",
		"status": "n"
	},
	"hk": {
		"name": "Hong Kong (English)",
		"status": "n"
	},
	"hk-zh": {
		"name": "Hong Kong (Chinese)",
		"status": "n"
	},
	"hu": {
		"name": "Hungary",
		"status": "n"
	},
	"id": {
		"name": "Indonesia",
		"status": "y"
	},
	"ie": {
		"name": "Ireland",
		"status": "n"
	},
	"it": {
		"name": "Italy",
		"status": "n"
	},
	"jp": {
		"name": "Japan",
		"status": "n"
	},
	"kr": {
		"name": "South Korea",
		"status": "n"
	},
	"lu": {
		"name": "Luxembourg",
		"status": "n"
	},
	"mx": {
		"name": "Mexico",
		"status": "n"
	},
	"my": {
		"name": "Malaysia",
		"status": "n"
	},
	"nl": {
		"name": "Netherlands",
		"status": "n"
	},
	"no": {
		"name": "Norway",
		"status": "n"
	},
	"nz": {
		"name": "New Zealand",
		"status": "n"
	},
	"ph": {
		"name": "Philippines",
		"status": "n"
	},
	"pl": {
		"name": "Poland",
		"status": "n"
	},
	"pt": {
		"name": "Portugal",
		"status": "n"
	},
	"ru": {
		"name": "Russia",
		"status": "n"
	},
	"se": {
		"name": "Sweden",
		"status": "n"
	},
	"sg": {
		"name": "Singapore",
		"status": "n"
	},
	"th": {
		"name": "Thailand",
		"status": "n"
	},
	"th-en": {
		"name": "Thailand (English)",
		"status": "n"
	},
	"tr": {
		"name": "Turkey",
		"status": "n"
	},
	"tw": {
		"name": "Taiwan",
		"status": "n"
	},
	"uk": {
		"name": "United Kingdom",
		"status": "n"
	},
	"us": {
		"name": "United States",
		"status": "n"
	},
	"vn": {
		"name": "Vietnam",
		"status": "n"
	},
	"xf": {
		"name": "Canada (French)",
		"status": "n"
	}
}


def search():
    findName = input("Enter the name which you want to search: ")
    count = 0
    for key, item in countries.items():
        if item["name"].lower() == findName.lower():
            print("Details : {0} - {1}".format(key, item["name"]))
            count = count + 1
            if count == 0:
                print("no name found !! Try again. ")
                search()


if __name__ == '__main__':
    search()


https://istheapplestoredown.com/api/v1/status/worldwide

==============================================




