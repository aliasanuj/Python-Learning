#datatypes_strings.py
===============================
#What is String in Python --> 
#A string is a sequence of characters.
#A character is simply a symbol. For example, the English language has 26 characters.
#Computers do not deal with characters, they deal with numbers (binary).
#Even though you may see characters on your screen, internally it is stored and manipulated as a combination of 0's and 1's.
#This conversion of character to a number is called encoding, and the reverse process is decoding. ASCII and Unicode are some of the popular encoding used.
#In Python, string is a sequence of Unicode character.
#Unicode was introduced to include every character in all languages and bring uniformity in encoding. You can learn more about Unicode from here.

#How to create a string in Python -->
#Strings can be created by enclosing characters inside a single quote or double quotes.
#Even triple quotes can be used in Python but generally used to represent multiline strings and docstrings.

# all of the following are equivalent
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
#When you run the program, the output will be:
Hello
Hello
Hello
Hello, welcome to
           the world of Python

#How to access characters in a string -->
#We can access individual characters using indexing and a range of characters using slicing.
#Index starts from 0. Trying to access a character out of index range will raise an IndexError.
#The index must be an integer. We can't use float or other types, this will result into TypeError.
#Python allows negative indexing for its sequences.
#The index of -1 refers to the last item, -2 to the second last item and so on.
#We can access a range of items in a string by using the slicing operator (colon).

str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
#str =  programiz
#str[0] =  p
#str[-1] =  z
#str[1:5] =  rogr
#str[5:-2] =  am

If we try to access index out of the range or use decimal number, we will get errors.
# index must be in range
>>> my_string[15]  
IndexError: string index out of range
# index must be an integer
>>> my_string[1.5] 
TypeError: string indices must be integers

#How to change or delete a string -->
#Strings are immutable.
#This means that elements of a string cannot be changed once it has been assigned.
#We can simply reassign different strings to the same name.

#Concatenation of Two or More Strings -->
#Joining of two or more strings into a single one is called concatenation.
#The + operator does this in Python. Simply writing two string literals together also concatenates them.
#The * operator can be used to repeat the string for a given number of times.

str1 = 'Hello'
str2 ='World!'
# using +
print('str1 + str2 = ', str1 + str2)
# using *
print('str1 * 3 =', str1 * 3)
#str1 + str2 =  HelloWorld!
#str1 * 3 = HelloHelloHello

#Iterating Through String -->
#Using for loop we can iterate through a string. Here is an example to count the number of 'l' in a string.
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
#3 letters found

#String Membership Test
#We can test if a sub string exists within a string or not, using the keyword in.
>>> 'a' in 'program'
True
>>> 'at' not in 'battle'
False

#Built-in functions to Work with Python -->
#Various built-in functions that work with sequence, works with string as well.
#Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object.
#It contains the index and value of all the items in the string as pairs. This can be useful for iteration.
#Similarly, len() returns the length (number of characters) of the string.

str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))
for i in enumerate(str):
    print(i)

#list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
#len(str) =  4
#(0, 'c')
#(1, 'o')
#(2, 'l')
#(3, 'd')

#Escape Sequence -->
#If we want to print a text like -He said, "What's there?"- we can neither use single quote or double quotes.
#This will result into SyntaxError as the text itself contains both single and double quotes.
#>>> print("He said, "What's there?"")
SyntaxError: invalid syntax
#>>> print('He said, "What's there?"')
SyntaxError: invalid syntax

#One way to get around this problem is to use triple quotes. Alternatively, we can use escape sequences.
#An escape sequence starts with a backslash and is interpreted differently.
#If we use single quote to represent a string, all the single quotes inside the string must be escaped.
#Similar is the case with double quotes. 

# using triple quotes
print('''He said, "What's there?"''')
# escaping single quotes
print('He said, "What\'s there?"')
# escaping double quotes
print("He said, \"What's there?\"")
#He said, "What's there?"
#He said, "What's there?"
#He said, "What's there?"

#Here is a list of all the escape sequence supported by Python.
#Escape Sequence in Python
#Escape Sequence	Description
#\newline		Backslash and newline ignored
#\\		Backslash
#\'		Single quote
#\"		Double quote
#\a		ASCII Bell
#\b		ASCII Backspace
#\f		ASCII Formfeed
#\n		ASCII Linefeed
#\r		ASCII Carriage Return
#\t		ASCII Horizontal Tab
#\v		ASCII Vertical Tab
#\ooo		Character with octal value ooo
#\xHH		Character with hexadecimal value HH

#Raw String to ignore escape sequence -->
#Sometimes we may wish to ignore the escape sequences inside a string.
#To do this we can place r or R in front of the string.
#This will imply that it is a raw string and any escape sequence inside it will be ignored.
#>>> print("This is \x61 \ngood example")
#This is a
#good example
#>>> print(r"This is \x61 \ngood example")
#This is \x61 \ngood example

#The format() Method for Formatting Strings
#The format() method that is available with the string object is very versatile and powerful in formatting strings.
#Format strings contains curly braces {} as placeholders or replacement fields which gets replaced.
#We can use positional arguments or keyword arguments to specify the order.

default_order = "{}, {} and {}".format('John','Bill','Sean')
print('--- Default Order ---')
print(default_order)
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('--- Positional Order ---')
print(positional_order)
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('--- Keyword Order ---')
print(keyword_order)
#--- Default Order ---
#John, Bill and Sean
#--- Positional Order ---
#Bill, John and Sean
#--- Keyword Order ---
#Sean, Bill and John

#The format() method can have optional format specifications.
#They are separated from field name using colon.
#For example, we can left-justify <, right-justify > or center ^ a string in the given space.
#We can also format integers as binary, hexadecimal etc. and floats can be rounded or displayed in the exponent format.
#There are a ton of formatting you can use. Visit here for all the string formatting available with the format() method.

>>> # formatting integers
>>> "Binary representation of {0} is {0:b}".format(12)
'Binary representation of 12 is 1100'
>>> # formatting floats
>>> "Exponent representation: {0:e}".format(1566.345)
'Exponent representation: 1.566345e+03'
>>> # round off
>>> "One third is: {0:.3f}".format(1/3)
'One third is: 0.333'
>>> # string alignment
>>> "|{:<10}|{:^10}|{:>10}|".format('butter','bread','ham')
'|butter    |  bread   |       ham|'

#Old style formatting
#We can even format strings like the old sprintf() style used in C programming language. We use the % operator to accomplish this.
#>>> x = 12.3456789
#>>> print('The value of x is %3.2f' %x)
#The value of x is 12.35
#>>> print('The value of x is %3.4f' %x)
#The value of x is 12.3457

===============================
a = "Hello, World!"
print(a[1])
#e
=======================
b = "Hello, World!"
print(b[2:5])
#llo
=======================
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
#Hello, World!
=======================
a = "Hello, World!"
print(len(a))
#13
========================
a = "Hello, World!"
print(a.lower())
#hello, world!
========================
a = "Hello, World!"
print(a.upper())
#HELLO, WORLD!
========================
a = "Hello, World!"
print(a.replace("H", "J"))
#Jello, World!
=========================
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#['Hello', ' World!']
=========================
print("Enter your name:")
x = input()
print("Hello, " + x)
#Enter your name:
# anuj
#Hello, anuj
==========================
my_string = 'Hello'
print(my_string)
my_string = "Hello"
print(my_string)
my_string = '''Hello'''
print(my_string)
# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
#Hello
#Hello
#Hello
#Hello, welcome to
#           the world of Python
===========================
str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
#str =  programiz
#str[0] =  p
#str[-1] =  z
#str[1:5] =  rogr
#str[5:-2] =  am
=============================
# index must be in range
>>> my_string[15]  
...
IndexError: string index out of range
# index must be an integer
>>> my_string[1.5] 
...
TypeError: string indices must be integers
================================
my_string = 'programiz'
my_string[5] = 'a'
print(my_string)
#TypeError: 'str' object does not support item assignment
=================================
my_string = 'programiz'
my_string[5] = 'a'
del my_string[1]
#TypeError: 'str' object does not support item assignment
=================================
str = 'programiz'
print('str = ', str)
#first character
print('str[0] = ', str[0])
#last character
print('str[-1] = ', str[-1])
#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])
#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])
#str =  programiz
#str[0] =  p
#str[-1] =  z
#str[1:5] =  rogr
#str[5:-2] =  am
===================================
str1 = 'Hello'
str2 ='World!'
# using +
print('str1 + str2 = ', str1 + str2)
# using *
print('str1 * 3 =', str1 * 3)
#str1 + str2 =  HelloWorld!
#str1 * 3 = HelloHelloHello
==================================
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')
#3 letters found
=================================
print('a' in 'program')
#True
=================================
print('at' not in 'battle')
#False
=================================
str = 'cold'
# enumerate()
list_enumerate = list(enumerate(str))
print('list(enumerate(str) = ', list_enumerate)
#character count
print('len(str) = ', len(str))
#list(enumerate(str) =  [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
#len(str) =  4
===================================
# using triple quotes
print('''He said, "What's there?"''')
# escaping single quotes
print('He said, "What\'s there?"')
# escaping double quotes
print("He said, \"What's there?\"")
#He said, "What's there?"
#He said, "What's there?"
#He said, "What's there?"
=====================================
Escape Sequence	Description
=====================================
\newline	Backslash and newline ignored
\\	Backslash
\'	Single quote
\"	Double quote
\a	ASCII Bell
\b	ASCII Backspace
\f	ASCII Formfeed
\n	ASCII Linefeed
\r	ASCII Carriage Return
\t	ASCII Horizontal Tab
\v	ASCII Vertical Tab
\ooo	Character with octal value ooo
\xHH	Character with hexadecimal value HH
=========================================
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")
#This is a 
#good example
#This is \x61 \ngood example
==========================================
# default(implicit) order
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Default Order ---')
print(default_order)
# order using positional argument
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)
# order using keyword argument
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)
#--- Default Order ---
#John, Bill and Sean

#--- Positional Order ---
#Bill, John and Sean

#--- Keyword Order ---
#Sean, Bill and John
==========================================
x = 12.3456789
print('The value of x is %3.2f' %x)
#The value of x is 12.35
print('The value of x is %3.4f' %x)
#The value of x is 12.3457
===========================================
astring = "Hello world!"
print("single quotes are ' '")
print(len(astring))
#single quotes are ' '
#12
==========================================
astring = "Hello world!"
print(astring.index("o"))
#4
==========================================
astring = "Hello world!"
print(astring.count("l"))
#3
==========================================
astring = "Hello world!"
print(astring[3:7])
#lo w
==========================================
astring = "Hello world!"
print(astring[3:7:2])
#1
========================================
astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
#lo w
#lo w
======================================
astring = "Hello world!"
print(astring[::-1])
#!dlrow olleH
======================================
astring = "Hello world!"
print(astring.upper())
print(astring.lower())
#HELLO WORLD!
#hello world!
===================================
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
#True
#False
================================
astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
#['Hello', 'world!']
==============================
s = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(s))
# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))
# Number of a's should be 2
print("a occurs %d times" % s.count("a"))
# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end
# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())
# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())
# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")
# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")
# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
#Length of s = 38
#The first occurrence of the letter a = 13
#a occurs 1 times
#The first five characters are 'Hey t'
#The next five characters are 'here!'
#The thirteenth character is 'h'
#The characters with odd index are 'e hr!wa hudti tigb?'
#The last five characters are 'g be?'
#String in uppercase: HEY THERE! WHAT SHOULD THIS STRING BE?
#String in lowercase: hey there! what should this string be?
#Split the words of the string: ['Hey', 'there!', 'what', 'should', 'this', 'string', 'be?']
========================================
Method	Description
========================================
capitalize()          Converts the first character to upper case
casefold()	           Converts string into lower case
center()	           Returns a centered string
count()	           Returns the number of times a specified value occurs in a string
encode()	           Returns an encoded version of the string
endswith()	           Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	           Searches the string for a specified value and returns the position of where it was found
format()	           Formats specified values in a string
format_map()	Formats specified values in a string
index()	           Searches the string for a specified value and returns the position of where it was found
isalnum()	           Returns True if all characters in the string are alphanumeric
isalpha()	           Returns True if all characters in the string are in the alphabet
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	           Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	           Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	           Returns True if all characters in the string are whitespaces
istitle()	           Returns True if the string follows the rules of a title
isupper()	           Returns True if all characters in the string are upper case
join()	           Joins the elements of an iterable to the end of the string
ljust()	           Returns a left justified version of the string
lower()	           Converts a string into lower case
lstrip()	           Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	           Returns a string where a specified value is replaced with a specified value
rfind()	           Searches the string for a specified value and returns the last position of where it was found
rindex()	           Searches the string for a specified value and returns the last position of where it was found
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	           Splits the string at the specified separator, and returns a list
rstrip()	           Returns a right trim version of the string
split()	           Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
swapcase()	           Swaps cases, lower case becomes upper case and vice versa
title()	           Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	           Converts a string into upper case
zfill()	           Fills the string with a specified number of 0 values at the beginning
=========================================
s.lower(), s.upper() --          returns the lowercase or uppercase version of the string
s.strip() --                     returns a string with whitespace removed from the start and end
s.isalpha()/s.isdigit()/s.isspace()... -- tests if all the string chars are in the various character classes
s.startswith('other'), s.endswith('other') -- tests if the string starts or ends with the given other string
s.find('other') --               searches for the given other string (not a regular expression) within s, and returns the first index where it begins or -1 if not found
s.replace('old', 'new') --       returns a string where all occurrences of 'old' have been replaced by 'new'
s.split('delim') --              returns a list of substrings separated by the given delimiter. The delimiter is not a regular expression, it's just text. 'aaa,bbb,ccc'.split(',') -> ['aaa', 'bbb', 'ccc']. As a convenient special case s.split() (with no arguments) splits on all whitespace chars.
s.join(list) --                  opposite of split(), joins the elements in the given list together using the string as the delimiter. e.g. '---'.join(['aaa', 'bbb', 'ccc']) -> aaa---bbb---ccc
===========================================
Format Symbol	Conversion
===========================================
%c	character
%s	string conversion via str() prior to formatting
%i	signed decimal integer
%d	signed decimal integer
%u	unsigned decimal integer
%o	octal integer
%x	hexadecimal integer (lowercase letters)
%X	hexadecimal integer (UPPERcase letters)
%e	exponential notation (with lowercase 'e')
%E	exponential notation (with UPPERcase 'E')
%f	floating point real number
%g	the shorter of %f and %e
%G	the shorter of %f and %E
==========================================
*	argument specifies width or precision
-	left justification
+	display the sign
<sp>	leave a blank space before a positive number
#	add the octal leading zero ( '0' ) or hexadecimal leading '0x' or '0X', depending on whether 'x' or 'X' were used.
0	pad from left with zeros (instead of spaces)
%	'%%' leaves you with a single literal '%'
(var)	mapping variable (dictionary arguments)
m.n.	m is the minimum total width and n is the number of digits to display after the decimal point (if appl.)
======================================
string.ascii_letters	           Concatenation of the ascii_lowercase and ascii_uppercase constants.
string.ascii_lowercase	Concatenation of lowercase letters
string.ascii_uppercase	Concatenation of uppercase letters
string.digits	Digit in strings
string.hexdigits	Hexadigit in strings
string.letters	concatenation of the strings lowercase and uppercase
string.lowercase	A string must contain lowercase letters.
string.octdigits	Octadigit in a string
string.punctuation	ASCII characters having punctuation characters.
string.printable	String of characters which are printable
String.endswith()	Returns True if a string ends with the given suffix otherwise returns False
String.startswith()	Returns True if a string starts with the given prefix otherwise returns False
String.isdigit()	Returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
String.isalpha()	Returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.
string.isdecimal()	Returns true if all characters in a string are decimal.
str.format()	one of the string formatting methods in Python3, which allows multiple substitutions and value formatting.
String.index	Returns the position of the first occurrence of substring in a string
string.uppercase	A string must contain uppercase letters.
string.whitespace	A string containing all characters that are considered whitespace.
string.swapcase()	Method converts all uppercase characters to lowercase and vice versa of the given string, and returns it
replace()	           returns a copy of the string where all occurrences of a substring is replaced with another substring.
======================================
BUILT-IN FUNCTION	DESCRIPTION
=======================================
string.Isdecimal	Returns true if all characters in a string are decimal
String.Isalnum	Returns true if all the characters in a given string are alphanumeric.
string.Istitle	Returns True if the string is a titlecased string
String.partition	splits the string at the first occurrence of the separator and returns a tuple.
String.Isidentifier	Check whether a string is a valid identifier or not.
String.len	           Returns the length of the string.
String.rindex	Returns the highest index of the substring inside the string if substring is found.
String.Max	           Returns the highest alphabetical character in a string.
String.min	           Returns the minimum alphabetical character in a string.
String.splitlines	Returns a list of lines in the string.
string.capitalize	Return a word with its first character capitalized.
string.expandtabs	Expand tabs in a string replacing them by one or more spaces
string.find	Return the lowest indexin a sub string.
string.rfind	find the highest index.
string.rindex	Raise ValueError when the substring is not found.
string.count	Return the number of (non-overlapping) occurrences of substring sub in string
string.lower	Return a copy of s, but with upper case letters converted to lower case.
string.split	Return a list of the words of the string,If the optional second argument sep is absent or None
string.rsplit()	Return a list of the words of the string s, scanning s from the end.
rpartition()	Method splits the given string into three parts
string.splitfields	Return a list of the words of the string when only used with two arguments.
string.join	Concatenate a list or tuple of words with intervening occurrences of sep.
string.strip()	It return a copy of the string with both leading and trailing characters removed
string.lstrip	Return a copy of the string with leading characters removed.
string.rstrip	Return a copy of the string with trailing characters removed.
string.swapcase	Converts lower case letters to upper case and vice versa.
string.translate	translate the characters using table
string.upper	lower case letters converted to upper case.
string.ljust	left-justify in a field of given width.
string.rjust	Right-justify in a field of given width.
string.center()	Center-justify in a field of given width.
string-zfill	Pad a numeric string on the left with zero digits until the given width is reached.
string.replace	Return a copy of string s with all occurrences of substring old replaced by new.
================================================================







