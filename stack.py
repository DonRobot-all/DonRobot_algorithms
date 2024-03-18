class StackMax:
    def __init__(self) -> None:
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if len(self.items) == 0:
            print('error')
            return 0
        self.items.pop()

    def get_max(self):
        if len(self.items) == 0:
            print('None')
            return 0
        print(max(self.items))


stack = StackMax()
counts = int(input())
for count in range(counts):
    command = input().split()
    if command[0] == 'get_max':
        stack.get_max()
    if command[0] == 'pop':
        stack.pop()
    if command[0] == 'push':
        stack.push(int(command[1]))
