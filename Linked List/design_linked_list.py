class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return - 1
        current = self.head
        for _ in range(index + 1):
            current = current.next
        return current.val
        
    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        new_node.next = self.head.next
        self.head.next = new_node
        self.size += 1
        
    def addAtTail(self, val: int) -> None:
        new_node = ListNode(val)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        new_node = ListNode(val)
        current = self.head
        for _ in range(index):
            current = current.next
        new_node.next = current.next
        current.next = new_node
        self.size += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.head
        for _ in range(index):
            current = current.next
        if current.next:
            current.next = current.next.next
            self.size -= 1