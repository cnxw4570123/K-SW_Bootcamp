# 8.12
gen = (f'Got {num}' for  num in range(10))  # generator comprehension
print(type(gen))  # generator object
for inner_gen in gen:  # iterate generator
    print(inner_gen)
