"""s = "hello"
for i in range(len(s)-1, -1, -1):
    print(f"i = {i}, s[i] = {s[i]}") """

def reverse_list_manual(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    print(lst)

reverse_list_manual([1,2,3,4,5])
