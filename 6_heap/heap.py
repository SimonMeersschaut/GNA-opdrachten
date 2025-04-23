class Heap:
    def __init__(self):
        self.content = [None]
    
    def add(self, value):
        self.content.append(value)
        self.swim(len(self.content) - 1)

    def swim(self, index: int):
        while (index > 1 and self.content[index//2] < self.content[index]):
            self.content[index//2], self.content[index] = self.content[index], self.content[index//2]
            index = index//2
    
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
                rechterkind_is_groter = (self.content[kind_index] < self.content[kind_index+1])
                if rechterkind_is_groter:
                    kind_index += 1
            if not self.content[kind_index] > self.content[index]:
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