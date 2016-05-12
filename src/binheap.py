# coding=utf-8


class Binheap(object):

    def __init__(self, values=None):
        self.binheap = []
        self.root = None
        self.length = 0
        if values:
            for value in values:
                self.push(value)

    def _sort_up(self):
        idx = self.length
        self.binheap = [0] + self.binheap
        while idx // 2 > 0:
            if self.binheap[idx] > self.binheap[idx // 2]:
                temp_val = self.binheap[idx // 2]
                self.binheap[idx // 2] = self.binheap[idx]
                self.binheap[idx] = temp_val
            idx = idx // 2
        del self.binheap[0]
        self.root = self.binheap[0]

    def push(self, value):
        self.binheap.append(value)
        self.length += 1
        self._sort_up()

    def pop(self):
        pop_val = self.binheap[0]
        self.length -= 1
        self.binheap[0] = self.binheap[-1]
        del self.binheap[-1]
        self._sort_down()
        return pop_val

    def _sort_down(self):
        idx = 1
        self.binheap = [0] + self.binheap
        while idx * 2 < self.length:
            comp_idx = self._max_child(idx)
            temp_val = self.binheap[comp_idx]
            if self.binheap[idx] < temp_val:
                self.binheap[comp_idx] = self.binheap[idx]
                self.binheap[idx] = temp_val
            idx = comp_idx
        del self.binheap[0]

    def _max_child(self, idx):
        if (idx * 2 + 1) > self.length:
            return idx * 2
        else:
            if self.binheap[idx * 2] > self.binheap[idx * 2 + 1]:
                return idx * 2
            else:
                return idx * 2 + 1
