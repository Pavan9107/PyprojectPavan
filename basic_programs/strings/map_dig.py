s = "1234abcd"

nums = s[:4]
print(nums)

chars = s[4:]
print(chars)

for i in range(len(nums)):
    print(nums[i], ":", chars[i])