
#217. Contains Duplicate


# Example input array
nums = [1, 2, 3, 4, 1]

# Check for duplicates
if len(nums) != len(set(nums)):
    print(True)
else:
    print(False)