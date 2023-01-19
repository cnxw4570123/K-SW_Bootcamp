def a():  # generator
    yield 1
    yield 2
    yield 3


def b():  # normal function
    return 1  # stop iteration
    return 2
    return 3


print(a(), b())
c = a()
print(c)
for i in c:
    print(i)
for i in c:
    print(i)

genobj = (pair for pair in zip(['a', 'b'], ['1', '2']))  # generator comprehension
print(genobj)

for thing in genobj:
    print(thing)