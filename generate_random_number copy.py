# number = 0
# array = [number := number + 1 for i in range(20000)]
# # with open('array_numbers.txt', 'w') as file:
# #     file.write(str(array))
# numbers = ' \npush '.join(map(str, array))
# with open('numbers_push.txt', 'w') as file:
#     file.write(numbers)


# number = 20000
# array = [number := number + 1 for i in range(10000)]
# # with open('array_numbers.txt', 'w') as file:
# #     file.write(str(array))
# numbers = ' \nget_max \npush '.join(map(str, array))
# with open('numbers_push.txt', 'a') as file:
#     file.write(numbers)


number = 20000
array = [number := number + 1 for i in range(10000)]
# with open('array_numbers.txt', 'w') as file:
#     file.write(str(array))
numbers = ' \n'.join(map(str, array))
with open('numbers_push.txt', 'w') as file:
    file.write(numbers)
