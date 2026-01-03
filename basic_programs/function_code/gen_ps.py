# Call generator → paused
# next() → resumes → yield value → paused again



nums = [1, -2, 3, -4, 5]

def gen_func(nums):
    for i in nums:
        if i>0:
            yield i

g = gen_func(nums)
print(next(g))
print(next(g))
print(next(g))