"""a = 5
b = 10
t = (b,a)
a, b = 10 , 5
print(t)
print(a)
print(b)

t = (1,2,3)
def unpack_and_sum(t):
    a,b,c = t
    d=a+b+c
    return d
print(unpack_and_sum(t))


data = [(1, 2), (3, 4), (5, 6)]
d = []
for a,b in data:
    c = a+b
    d.append(c)

print(d)


data = [(1, 4), (3, 1), (5, 2)]
def sort_data(data):
    return sorted(data, key=lambda x:x[1])
print(sort_data(data))



data = [(1, 4), (2, 3), (3, 6), (4, 7)]

result = []
def sort_even_data(data):

    for a,b in data:
        if b%2==0:
            result.append((a,b))
    return result
print(sort_even_data(data))


data = [(1, 4), (2, 3), (3, 6), (4, 7)]


def sum_data(data):
    result = 0
    for i in data:
        result += sum(i)
    return result
print(sum_data(data))

data = [(1, 4), (2, 3), (3, 6), (4, 7)]

def highest_sum(data):
    max_sum = 0
    max_tup= None

    for i in data:
        current_sum = sum(i)
        if current_sum > max_sum:
            max_sum = current_sum
            max_tup = i
    return max_tup

print(highest_sum(data))


data = [(2, 4), (1, 6), (4, 8), (3, 5)]

def return_even_tup(data):
    z = []
    for a,b in data:
        if a%2==0 and b%2==0:
            z.append((a,b))
    return z

print(return_even_tup(data))


data = [(1, 2), (3, 4), (5, 6)]

def convert_to_list(data):
    l=[]
    for a,b in data:
        l.append(a)
        l.append(b)
    return l
print(convert_to_list(data))


lst = [1, 2, 2, 3, 4, 4, 5, 1]

def no_dup(lst):
    l = []
    for i in lst:
        if i not in l:
            l.append(i)
    return l
print(no_dup(lst))

print(set(lst))



data = [(3, 4), (1, 1), (5, 0), (2, 2)]

def find_tuples(data):
    min_sum = None
    min_tup = None
    for a,b in data:
        current_sum = a+b
        if min_sum is None or current_sum < min_sum:
            min_sum = current_sum
            min_tup = (a,b)
    return min_tup
print(find_tuples(data))


lst = [1, 2, 3, 4, 5]
def odd_numbers(data):
    return [x**2 for x in data if x%2!=0]
print(odd_numbers(lst))


data = [(2, 4), (1, 6), (4, 8), (3, 5)]

def even_tup(data):
    count = 0
    for a,b in data:
        if a% 2 == 0 and b%2==0:
            count +=   1
    return count
print(even_tup(data))
"""
data = [(2, 3), (4, 2), (3, 5), (6, 4)]
def sorted_list(data):
    l=[]
    for a,b in data:
        l.append(a)
        l.append(b)
    return sorted(set(l))
print(sorted_list(data))
