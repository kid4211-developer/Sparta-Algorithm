class LinkedTuple:
    def __init__(self):
        self.items = list()

    def add(self, key, value):
        self.items.append((key, value))

    def get(self, key):
        for k, v in self.items:
            if key == k:
                return v


# Chaining
class LinkedDict:
    def __init__(self):
        self.items = []  # items 배열에는 LinkedTuple() 총 8개 입력된 상태
        for index in range(8):
            self.items.append(LinkedTuple())

    def put(self, key, value):
        index = hash(key) % len(self.items)
        # 이미 비어있는 LinkedTuple 배열이 해당 index에 들어 있는 상태
        # 그래서 self.items[index] 자체가 그 LinkedTuple을 가르키므로
        # self.items[index].add(key, value)를 하게 되면 [(key, value)] 식으로 들어가게 된다
        self.items[index] = value

    def get(self, key):
        index = hash(key) % len(self.items)
        return self.items[index].get(key)
