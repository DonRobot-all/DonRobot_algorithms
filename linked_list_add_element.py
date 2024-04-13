class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


def print_node(vertex):
    while vertex:
        print(vertex.value, end=' ')
        vertex = vertex.next
    return None


def add_node(vertex, node, idx):
    idx -= 1
    while idx:
        vertex = vertex.next
        idx -=  1
    temp = vertex.next
    vertex.next = node
    vertex = vertex.next
    vertex.next = temp
    


new_n6 = Node('value3.1')
n5 = Node('value5')
n4 = Node('value4', n5)
n3 = Node('value3', n4)
n2 = Node('value2', n3)
n1 = Node('value1', n2)
print(print_node(n1))
add_node(n1, new_n6, 3)
print(print_node(n1))