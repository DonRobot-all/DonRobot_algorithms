class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.right = None
        self.left = None
        self.length = 0

    def get(self):
        if self.right is None:
            print('error')
            return 0
        temp = self.right
        self.right = self.right.next
        if self.right is None:
            self.left = None
        self.length -= 1
        print(temp.value)

    def put(self, x):
        node = Node(x)     
        if self.right is None:
            self.right = node
            self.left = node
        else:
            self.left.next = node
            self.left = node
        self.length += 1

    def size(self):
        print(self.length)


stack = Stack()
max_command = int(input())
for count in range(max_command):
    command = input().split()
    if command[0] == 'get':
        stack.get()
    if command[0] == 'size':
        stack.size()
    if command[0] == 'put':
        stack.put(int(command[1]))
