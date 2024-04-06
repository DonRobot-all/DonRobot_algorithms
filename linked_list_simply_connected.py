class Node:
    def __init__(self, value=None, next=None) -> None:
        self.value = value
        self.next = next


def print_node(vertex):
    # print(vertex.value)
    # print(vertex.next.value)
    # print(vertex.next.next.value)
    while vertex:
        print(vertex.value, end=' ')
        vertex = vertex.next
    return None

def del_node(vertex, idx):
    idx -= 1
    while idx:
        print(vertex.value)
        vertex = vertex.next
        idx -= 1
    vertex.next = vertex.next.next
    return vertex


n5 = Node('value5')
n4 = Node('value4', n5)
n3 = Node('value3', n4)
n2 = Node('value2', n3)
n1 = Node('value1', n2)
print(print_node(n1))
del_node(n1, 1)
print(print_node(n1))