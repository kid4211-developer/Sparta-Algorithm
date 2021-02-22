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


def get_linked_list_sum(list_1, list_2):
    node = list_1.head
    list1 = [str(node.data)]
    while node.next is not None:
        list1.append(str(node.next.data))
        node = node.next

    str1 = ''.join(list1)

    node = list_2.head
    list2 = [str(node.data)]
    while node.next is not None:
        list2.append(str(node.next.data))
        node = node.next

    str2 = ''.join(list2)

    result = int(str1) + int(str2)
    return result


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

# linked_list 에서 저장되어 알 수 있는 값은 node.head 이다.
print(get_linked_list_sum(linked_list_1, linked_list_2))