class Node:
    def __init__(self, value, next_item=None):
        self.value = value
        self.next_item = next_item


def solution(node, idx):
    head = node
    if idx == 0:
        head = node.next_item
        return head
    idx -= 1
    while idx:
        node = node.next_item
        idx -= 1
    node.next_item = node.next_item.next_item
    return head


def test():
    node3 = Node(input(), None)
    node2 = Node(input(), node3)
    node1 = Node(input(), node2)
    node0 = Node(input(), node1)
    new_head = solution(node0, int(input()))
    print(new_head.value,
          new_head.next_item.value, 
          new_head.next_item.next_item.value)


if __name__ == '__main__':
    test()
