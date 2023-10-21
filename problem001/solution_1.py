sum = 8

for i in range(6, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        sum += i

print(sum)