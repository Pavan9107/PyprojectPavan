"""
l = [1,1,2,3,4,4,5,5,6,6,6,7]
s =  set(l)
print(s)


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common_list = []
for i in list1:
    for j in list2:
        if i == j:
            common_list.append(j)

print(common_list)

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
common_set  = list(set(list1)&set(list2))
print(common_set)


str1 = set("listen")
str2 = set("silent")

if sorted(str1) == sorted(str2):
    print("Anagrams")
else:
    print("Not anagrams")

def has_duplicates(lst):
    return len(lst) != len(set(lst))
numbers = [1, 2, 3, 4, 5, 2]
print(has_duplicates(numbers))  # Output: True


nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = 10

def find_missing_number(nums, n):
    full_set = set(range(1,n+1))
    given_set = set(nums)
    missing_set = full_set - given_set
    return missing_set.pop()
print(find_missing_number(nums,n))


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A |B)
print(A & B)
print(A ^ B)
print(A - B)


from collections import defaultdict
print(defaultdict(list))
words = ["cat", "tac", "act", "dog", "god", "odg", "rat"]
"""


