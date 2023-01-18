# 8.13
# dict1 = dict()
# for key, value in zip(('optimist', 'pessimist', 'troll'),('The glass is half full', 'The glass is half empty', 'How did you get a glass?')):
#     dict1[key] = value

# print(dict1)
# dict1 = dict(zip(('optimist', 'pessimist', 'troll'),('The glass is half full', 'The glass is half empty', 'How did you get a glass?')))
# print(dict1)

keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full', 'The glass is half empty', 'How did you get a glass?')
dict1 = dict(zip(keys, values))
print(dict1)