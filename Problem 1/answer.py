nums = 1000
Sum = 0
for i in range(nums):
    if (i % 3 == 0) or (i % 5 == 0):
        Sum+=i

print(f"the sum of the multiples of 3 and 5 in the range of {nums} is: {Sum}")