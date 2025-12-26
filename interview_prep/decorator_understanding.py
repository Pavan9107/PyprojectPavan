def decorator_check(func):
    def check_m2():
        print('check')
        print(func())
        print("functionality in code")
    return check_m2

@decorator_check
def final_method():
    return 'decorator method'

final_method()

# #args and kwargs
# *args collects extra positional arguments into a tuple.
#
# **kwargs collects extra keyword arguments into a dict.
# They let a function accept variable arguments and are also used to unpack iterables/dicts when calling a function.
def show(a,b,*args, **kwargs):
    print(a, b, args, kwargs)

show(1,2,3,4, x=5, y=6)

labels = [((x,"even") if x%2==0 else (x,"odd")) for x in range(5)]
print(labels)