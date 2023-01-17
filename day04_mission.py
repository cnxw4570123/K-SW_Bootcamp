# Prob 8.4 ~ 8.5
e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

for eng_key in e2f:
    if e2f[eng_key] == 'chien':
        print(eng_key)

print('-----------------------')

for key in e2f.keys():
    print(key)