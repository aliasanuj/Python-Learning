number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#[-5, -4, -3, -2, -1]


number_list = range(-5, 5)
less_than_zero = list(map(lambda x: x < 0, number_list))
print(less_than_zero)
#[True, True, True, True, True, False, False, False, False, False]


#Map applies a function to all the items in an input_list. Here is the blueprint:
#map(function_to_apply, list_of_inputs)


#As the name suggests, filter creates a list of elements for 
#which a function returns true. Here is a short and concise example:


#Reduce is a really useful function for performing some computation on a list and
# returning the result. It applies a rolling computation to sequential pairs of
# values in a list. For example, if you wanted to compute the product of a list of integers.
#So the normal way you might go about doing this task in python is using a basic for loop:

product = 1
list = [1, 2, 3, 4]
for num in list:
    product = product * num
# product = 24
Now let’s try it with reduce:

from functools import reduce
product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
# Output: 24

from functools import reduce
product = reduce((lambda x, y: x * y), (1, 2, 3, 4))
print(product)
#24
