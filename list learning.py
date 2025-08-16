"""
fruits = ['apple', 'banana', 'cherry']

fruits.append('orange')
print(fruits)

fruits.extend('kiwi')
print(fruits)

for fruit in fruits:
    print(fruit)

# Cannot: point[0] = 10
# But can contain mutable elements
a = ([1, 2], 3)
a[0].append(4)  # Valid!
print(a)


total = 0
def sum_of_numbers(numbers):
    global total
    for number in numbers:
        total += number
    return total

sum_of_numbers([1, 2, 3])
print(total)

def reverse_a_list(l):
    return l[::-1]

print(reverse_a_list([1, 2, 3]))

l = [1,1,2,3,4,4,5,5,6,6,6,7]
d= []
for i in l:
    if i not in d:
        d.append(i)
print(d)


l = [4, 8, 3, 10, 1, 2]
max_value = l[0]  # Start with the first element

for i in l:
    if i > max_value:
        max_value = i

print(max_value)  # Output: 10



def even_squares():
    z = []
    for i in range(0,10):
        if i % 2 == 0:
            y = i ** 2
            z.append(y)
    return z
print(even_squares())

"""

def even_squares():
    return [i**2 for i in range(0,11) if i%2 == 0]
print(even_squares())