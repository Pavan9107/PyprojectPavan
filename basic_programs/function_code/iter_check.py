# 1️⃣ Iterable vs Iterator (VERY IMPORTANT)
# Iterable
#
# 👉 Something you can loop over
# Examples: list, tuple, string


nums = [1, 2, 3]

# Iterator
#
# 👉 Object that gives values one at a time
it =  iter(nums)
print(next(it))
print(next(it))
print(next(it))

