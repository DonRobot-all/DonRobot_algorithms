class StackMax:
    def __init__(self) -> None:
        self.items = []
        self.max_array = []

    def push(self, x):
        self.items.append(x)
        if len(self.max_array) == 0:
            self.max_array.append(x)
        elif x >= self.max_array[-1]:
            self.max_array.append(x)

    def pop(self):
        items_len = len(self.items)
        if items_len == 0:
            print('error')
            return 0
        if len(self.max_array) != 0 and self.items[items_len - 1] == self.max_array[-1]:
            del self.max_array[-1]
        del self.items[items_len - 1]

    def top(self):
        if len(self.items) == 0:
            print('error')
            return 0
        print(self.items[-1])
        return self.items[-1]

    def get_max(self):
        if len(self.items) == 0:
            print('None')
            return 0
        if len(self.max_array) == 0:
            print(max(self.items))
            return max(self.items)
        print(self.max_array[-1])


stack = StackMax()
counts = int(input())
for count in range(counts):
    command = input().split()
    if command[0] == 'get_max':
        stack.get_max()
    if command[0] == 'pop':
        stack.pop()
    if command[0] == 'top':
        stack.top()
    if command[0] == 'push':
        stack.push(int(command[1]))
