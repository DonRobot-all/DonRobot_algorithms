"""
Считываем данные
"""

distances = []
for i in range(2):
    distances.append([int(i) for i in input().split()])
print(distances)

distances = [[int(i) for i in input().split()] for _ in range(2)]
print(distances)
