# Prob 7.11
start1 = ['fee', 'fie', 'foe']
rhymes = [
    ('flop', 'get a mop'),
    ('fope', 'turn the rope'),
    ('fa', 'get your ma'),
    ('fudge', 'call your ma'),
    ('fat', 'pet the cat'),
    ('fog', 'walk the dog'),
    ('fun', 'say we\'re done'),
]
start2 = 'Someone better'

for rhymeH, rhymeB in rhymes:
    for st1_word in start1:
        print(f'{st1_word.title()}!', end=' ')
    print(f'{rhymeH.title()}!')  # unpacking
    print(f'{start2} {rhymeB}')
