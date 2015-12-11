#判断 Iterable 属于哪种类型
from collections import Iterable 
#list
b = isinstance([], Iterable)
print(b)

#dist
b = isinstance({}, Iterable)
print(b)

#str
b = isinstance('abc', Iterable)
print(b)

#generator
b = isinstance((x for x in range(10)), Iterable)
print(b)

#int
b = isinstance(100, Iterable)
print(b)

