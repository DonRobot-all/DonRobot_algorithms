class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self) -> None:
        self.tail = None
        self.head = None
        self.length = 0

    def put(self, x):
        node = Node(x)
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            print(self.head.value, self.head.next.value)
            self.head = node
            print(self.head.value, self.tail.value)
        self.length += 1

    def get(self):
        if self.length != 0:
            print(self.tail.value)
            self.tail = self.tail.next
            print(self.tail.value)

    


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
