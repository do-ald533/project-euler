palindrom_list = [i*j for i in range(100, 999+1) for j in range(100, 999+1)]

result = 0

for nums in palindrom_list:
    if ((nums := str(nums)) == nums[::-1]):
        nums = int(nums)
        if ((result) < nums):
            result = nums
print(result)
