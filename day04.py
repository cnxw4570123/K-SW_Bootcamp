# list comprehension

# odd_list = []
# for i in range(0, 11):
#     if i % 2 == 1:
#         odd_list.append(i)
odd_list = [odd_num for odd_num in range(1, 11) if odd_num % 2 == 1]
odd_tuple = (odd_num for odd_num in range(1, 11) if odd_num % 2 == 1)
print(odd_list, type(odd_list))
print(odd_tuple, type(odd_tuple))

print(type(range(1, 101))) # 생성해주지 않는다