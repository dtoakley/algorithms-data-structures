
class BinaryHeap(object):

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def _percolate_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]

            i //= 2

    def _percolate_down(self, i):
        while (i * 2) < self.current_size:
            min_child = self._min_child(i)
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]

            i = min_child

    def _min_child(self):
        if i * 2 + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self._percolate_up(self.current_size)

    def del_min(self):
        return_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size += 1
        self.heap_list.pop()
        self._percolate_down(1)
        return return_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.current_size = len(a_list)
        self.heap_list = [0] + a_list[:]
        while i > 0:
            self._percolate_down(i)
            i -= i




