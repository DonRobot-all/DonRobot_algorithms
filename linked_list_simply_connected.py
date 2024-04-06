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


n3 = Node('value3')
n2 = Node('value2', n3)
n1 = Node('value1', n2)
print(print_node(n1))
print(print_node(n1))