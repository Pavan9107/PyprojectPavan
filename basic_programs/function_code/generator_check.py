#Generator = function that remembers state and uses yield

def get_number():
    yield 1
    yield 2
    yield 3

g= get_number()
print(next(g))
print(next(g))
print(next(g))
