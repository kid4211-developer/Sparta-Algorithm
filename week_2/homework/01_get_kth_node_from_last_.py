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

    def get_kth_node_from_last(self, k):
        count = self.get_node_count()
        index = count - k
        return self.get_node(index)

    def get_node_count(self):
        index = 1
        cur = self.head
        while cur.next is not None:
            cur = cur.next
            index = index + 1
        return index

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


linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
linked_list.append(10)

print(linked_list.get_kth_node_from_last(2).data)  # 7이 나와야 합니다!
