class PriorityQueue:
    def __init__(self):
        self.__binary_heap = [0]
        self.__size = len(self.__binary_heap) - 1

    def __str__(self):
        return f"{self.__binary_heap}"

    def __len__(self):
        return self.__size

    def add_all(self, a_list):
        for elements in a_list:
            self.__binary_heap.append(elements)
        self.__size = len(self.__binary_heap) - 1

    def percolate_up(self, index):
        while index // 2 > 0:
            if self.__binary_heap[index] < self.__binary_heap[index // 2]:
                current_node = self.__binary_heap[index]
                parent_node = self.__binary_heap[index // 2]
                self.__binary_heap[index // 2] = current_node
                self.__binary_heap[index] = parent_node
            index = index // 2

    def insert(self, element):
        self.__binary_heap.append(element)
        self.__size += 1
        self.percolate_up(self.__size)

    def get_smaller_child_index(self, index):
        if index * 2 + 1 > self.__size:
            return index * 2
        else:
            child1 = self.__binary_heap[index * 2 ]
            child2 = self.__binary_heap[index * 2 + 1]
            return self.__binary_heap.index(min(child1, child2))

    def percolate_down(self, index):
        while index * 2 <= self.__size:
            smallest_child = self.get_smaller_child_index(index)
            if self.__binary_heap[index] > self.__binary_heap[smallest_child]:
                current_node = self.__binary_heap[index]
                child_node = self.__binary_heap[smallest_child]
                self.__binary_heap[smallest_child] = current_node
                self.__binary_heap[index] = child_node
            index *= 2

    def create_heap_fast(self, values):
        self.add_all(values)
        for i in range(self.__size // 2, 0, -1):
            print(self.__binary_heap)
            self.percolate_down(i)


def main():
    pq = PriorityQueue()
    keys = [9, 5, 8, 6, 3, 2]
    pq.create_heap_fast(keys)
    print(pq)
    return

main()