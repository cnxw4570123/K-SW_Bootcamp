# tuple

a = 'harry',
b = ('harry',)
c = ()  # empty tuple
d = 'harry', 'ron'  # packing
e = ('hermione')  # string
f = ('harry', 'ron')
g = ('hermione',)  # string
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(f[0])
x, y = f  # unpacking
print(x)
print(y)
print(g + f)
h = g + f
print(h)
print(id(g))
g = g + f
print(id(g))

print(g)  # overwrite
