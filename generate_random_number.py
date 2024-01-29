import random
number = 0
array = [number := number + random.randint(0, 100) for i in range(200000)]
# with open('array_numbers.txt', 'w') as file:
#     file.write(str(array))
numbers = ' '.join(map(str, array))
with open('numbers.txt', 'w') as file:
    file.write(numbers)
