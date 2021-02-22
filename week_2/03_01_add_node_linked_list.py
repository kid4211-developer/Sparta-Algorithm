class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        count = 0
        cur = self.head
        while cur is not None:
            if count != index:
                count += 1
                cur = cur.next
            else:
                break
        return cur

    def add_node(self, index, value):
        count = 0
        node = self.head
        changed_node = self.get_node(index)
        while node is not None:
            if index == 0:
                self.head = Node(value)
                node = self.head
                node.next = changed_node
                break
            else:
                if count == (index - 1):
                    node.next = Node(value)
                    node = node.next
                    node.next = changed_node
                    break
                else:
                    count += 1
                    node = node.next


linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(24)
linked_list.append(3)
linked_list.add_node(0, 70)
linked_list.print_all()