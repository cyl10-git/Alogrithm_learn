class Node:
    '''建立Node类'''
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class MyLinkedList:
    '''创建结构'''
    def __init__(self) -> None:
        self.head = Node(-1)
        self.size = 0

def get(self, index: int) -> int:
    '''获取单链表中第index个节点'''
    if index < 0:
        return -1
    p = self.head
    for i in range (index + 1):
        p = p.next
    if p == None:
        return -1
    return p.val

def addAtIndex(self, index: int, val: int) -> None:
    if index > self.size:
        return
    if index < 0:
        index = 0
    p = self.head
    for i in range(index):
        p = p.next
    #   添加节点
    temp_node = Node(val)
    temp_node.next = p.next
    p.next = temp_node

    self.size += 1
