class Node:
    def __init__(self, value=None, next=None, previus=None) -> None:
        self.value = value
        self.previus = previus
        self.next = next

def print_node(vertex):
    while vertex:
        print(vertex.value, end=' ')
        vertex = vertex.next
    return None


def print_node_back(vertex):
    while vertex.next:
        vertex = vertex.next
    while vertex:
        print(vertex.value, end=' ')
        vertex = vertex.previus
    return None

n5 = Node('value5')
n4 = Node('value4', n5)
n3 = Node('value3', n4)
n2 = Node('value2', n3)
n1 = Node('value1', n2)
n5.previus = n4
n4.previus = n3
n3.previus = n2
n2.previus = n1
print_node(n1)
print()
print_node_back(n1)
