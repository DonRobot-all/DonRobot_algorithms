class MyQueueSized:
    def __init__(self, max_size) -> None:
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.length = 0

    def push(self, x):
        if self.length != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.length += 1
            return 0
        print('error')

    def pop(self):
        if self.length == 0:
            print('None')
            return 'None'
        return_element = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.length -= 1
        print(return_element)
        return return_element

    def size(self):
        print(self.length)
        return self.length

    def peek(self):
        if self.length == 0:
            print('None')
            return 0
        print(self.queue[self.head])


max_command = int(input())
max_size = int(input())
stack = MyQueueSized(max_size)
for count in range(max_command):
    command = input().split()
    if command[0] == 'peek':
        stack.peek()
    if command[0] == 'pop':
        stack.pop()
    if command[0] == 'size':
        stack.size()
    if command[0] == 'push':
        stack.push(int(command[1]))
