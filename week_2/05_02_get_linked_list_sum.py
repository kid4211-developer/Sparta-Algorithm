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


# linkedList의 값들을 숫자로 변환해줄때 x 10을 해주면 자릿수가 맞춰진다
def get_linked_list_sum(list_1, list_2):
    sum_1 = _get_linked_list_sum(list_1)
    sum_2 = _get_linked_list_sum(list_2)

    result = sum_1 + sum_2
    return result


def _get_linked_list_sum(linked_list):
    linked_list_sum = 0
    node = linked_list.head
    while node is not None:
        linked_list_sum = linked_list_sum * 10 + node.data
        node = node.next
    return linked_list_sum


linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

# linked_list 에서 저장되어 알 수 있는 값은 node.head 이다.
print(get_linked_list_sum(linked_list_1, linked_list_2))