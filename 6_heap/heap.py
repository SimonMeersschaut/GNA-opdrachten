class Heap:
    def __init__(self):
        self.content = [None]
        self.count = 0
    
    def add(self, value):
        self.content.append(value)
        self.swim(len(self.content) - 1)

    def swim(self, index: int):
        while (index > 1 and self.less(index//2, index)):
            self.content[index//2], self.content[index] = self.content[index], self.content[index//2]
            index = index//2
    
    def less(self, index1, index2):
        self.count += 1
        return self.content[index1] < self.content[index2]

    def grab_count(self):
        value = self.count
        self.count = 0
        return value
    
    def delete_max(self):
        # swap root with last element
        self.content[1], self.content[-1] = self.content[-1], self.content[1]
        # delete last element and store value
        value = self.content.pop(-1)
        # sink root
        self.sink(1)
        #
        return value
    
    def sink(self, index: int):
        while 2*index <= len(self.content) - 1:
            kind_index = 2*index
            if (kind_index < len(self.content) - 1):
                rechterkind_is_groter = self.less(kind_index, kind_index+1)
                if rechterkind_is_groter:
                    kind_index += 1
            if not self.less(index, kind_index):
                break
            # exchange
            self.content[kind_index], self.content[index] = self.content[index], self.content[kind_index]
            index = kind_index

if __name__ == '__main__':
    h = Heap()
    for i in range(10):
        h.add(i)
    print(h.content)
    h.delete_max()
    print(h.content)