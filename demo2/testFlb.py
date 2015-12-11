# 斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

# fib(5)

# generator
# 如果一个函数定义中包含了 yield 关键字 这个函数就不是普通的函数 而是一个generator
# 这里，generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 例如下面：odd()


def fib2(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib2(6)
# print(next(f))


def odd():
    k = 0
    print(k)
    k = k + 1
    yield 1
    k = k + 1
    print(k)
    yield 3
    print(k)
    yield 5
    return 'done'

# 这是一个generator
g = odd()

# 利用next 来执行generator 但是只能只能一次
# print(next(g))

# 利用 for 循环 来执行generator  但无法获取返回值
# for n in g:
# print(n)

# 利用while 循环来执行 next
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('return value', e.value)
        break

# 杨辉三角


# def triangles():
#     b = [1, ]
#     while(True):
#         yield b
#         i = len(b) - 1
#         while(i):
#             b[i] = b[i] + b[i - 1]
#             i -= 1
#         b.append(1)

def triangles():
    b = [1]
    while True:
        yield b
        b = [1] + [b[i] + b[i+1] for i in range(len(b)-1)] + [1]

k = 0
for n in triangles():
    print(n)
    k=k+1
    if k==10:
        break


