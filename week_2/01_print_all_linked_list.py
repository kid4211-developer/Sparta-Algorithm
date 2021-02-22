# Node는 값인 data와 다음 node를 가르키는 next가 있어야 함
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # 최소 생성시엔 가르키는게 없기 때문


# Node를 생성해 headNode로 설정 해줌
class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)
        # print(cur.data)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


linked_list = LinkedList(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.print_all()
