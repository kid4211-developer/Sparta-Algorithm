class MaxHeap:
    def __init__(self):
        self.items = [None]

    # 1. new Node를 맨밑에 추가한다.
    # 2. 지금 넣은 new Node를 부모와 비교하고, 만약 부모보다 크다면 교체해준다.
    # 3. 이 과정을 최상위 레벨까지 반복한다.
    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1
        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[cur_index], self.items[parent_index] = self.items[parent_index], self.items[cur_index]
                cur_index = parent_index
            else:
                break
        return


max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!