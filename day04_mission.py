# Prob 8.3
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

f2e = dict()
print(f2e)
for eng_key, eng_val in e2f.items():
    f2e[eng_val] = eng_key
print(f2e)