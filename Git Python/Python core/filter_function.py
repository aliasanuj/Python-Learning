#filter_function.py
========================
number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#[-5, -4, -3, -2, -1]
==========================
def fun(variable): 
    letters = ['a', 'e', 'i', 'o', 'u'] 
    if (variable in letters): 
        return True
    else: 
        return False
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
filtered = filter(fun, sequence) 
print('The filtered letters are:') 
for s in filtered: 
    print(s) 
#e
#e
==========================
seq = [0, 1, 2, 3, 5, 8, 13] 
result = filter(lambda x: x % 2, seq) 
print(list(result)) 
result = filter(lambda x: x % 2 == 0, seq) 
print(list(result)) 
#[1, 3, 5, 13]
#[0, 2, 8]
===========================
randomList = [1, 'a', 0, False, True, '0']
filteredList = filter(None, randomList)
print('The filtered elements are:')
for element in filteredList:
    print(element)
#The filtered elements are:
#1
#a
#True
#0
==============================
ages = [5, 12, 17, 18, 24, 32]
def myFunc(x):
  if x < 18:
    return False
  else:
    return True
adults = filter(myFunc, ages)
for x in adults:
  print(x)
#18
#24
#32
==============================
list1 = [1,2,3,6,5,4,7,8,9]
result = map(lambda x : x>5,list1)
print(list(result))
#[False, False, False, True, False, False, True, True, True]
==============================
