"""
map is lazy and only evaluates the result when iterated over - generator
map will stop when the smallest input is out
- not faster the list comprehensive
"""
t = map(ord, 'Hello World')
print(t)
print(next(t))
for i in t:
    print(i)


def foo(x, y, z):
    print(x, y, z)


a, b, c = ['a1', 'a2'], ['b1', 'b2'], ['c1', 'c2']

b = map(foo, a, b, c)
list(b)
