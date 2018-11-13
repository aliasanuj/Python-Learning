number_list = range(-5, 5)
less_than_zero = list(filter(lambda x: x < 0, number_list))
print(less_than_zero)
#[-5, -4, -3, -2, -1]


number_list = range(-5, 5)
less_than_zero = list(map(lambda x: x < 0, number_list))
print(less_than_zero)
#[True, True, True, True, True, False, False, False, False, False]



