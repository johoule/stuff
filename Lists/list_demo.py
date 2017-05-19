# make a list
nums = [3, 1, 4, 1, 5, 9]

# find the length of a list
print( len(nums) )

# select individual items from a list
begin = nums[0]
end = nums[-1]

print(begin, end)

# get a "slice" of a list
print( nums[:3] )
print( nums[3:] )
print( nums[2:4] )

# lists can contain strings
names = ["Terry Gilliam", "Michael Palin", "Eric Idle", "Terry Jones", "John Cleese", "Graham Chapman"]
print(len(names))
print(names)

# select a random element from a list
import random
print(random.choice(names))


