class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head

    # pop -> 기존의 head는 없애주고 그다음 Node를 head로 교체
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        delete_head = self.head
        self.head = self.head.next
        return delete_head

    # peek -> head의 값을 반환
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.head.data

    # isEmpty -> head가 None 인지 아닌지 판별
    def is_empty(self):
        return self.head is None


stack = Stack()
stack.push(3)
print(stack.peek())
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())
print(stack.is_empty())