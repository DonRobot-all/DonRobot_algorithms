import sys
# name = input('Привет, как тебя зовут')
# print(f'тебя зовут {name}')


# name = sys.stdin.readline()
# print(f'тебя зовут {name}')

# for i in range(10**6):
#     input()

# for i in range(10**6):
#     sys.stdin.readline().rstrip()

# print('привет')
# print('следующая строчка')
# print('следующая строчка')
# print('следующая строчка')
# print('привет\nследующая строчка\nследующая строчка\nследующая строчка')
# number = sys.stdin.readline().rstrip()
# number = number.split()
# print(number)
# print(type(number))

a = int(sys.stdin.readline().rstrip())
c = [None] * a
for i in range(int(a)):
    b = sys.stdin.readline().rstrip()
    b = b.split()
    b = str(int(b[0]) + int(b[1]))
    c[i] = b
print('\n'.join(c))
