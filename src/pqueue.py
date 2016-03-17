class Pqueue(object):

    def __init__(self, item):
        self.pqueue = []
        self.insert(item)

    def insert(self, item):
        for pair in item:
            self.pqueue.append(pair)
            self._sort_up()

    def _sort_up(self):
        idx = len(self.pqueue) - 1
        while (idx-1)//2 >= 0:
            if self.pqueue[idx][0] > self.pqueue[(idx-1)//2][0]:
                temp_parent = self.pqueue[(idx-1)//2]
                self.pqueue[(idx-1)//2] = self.pqueue[idx]
                self.pqueue[idx] = temp_parent
            idx = (idx-1)//2

    def pop(self):
        root = self.pqueue[0]
        self.pqueue[0] = self.pqueue[-1]
        self.pqueue.remove(self.pqueue[-1])
        self._sort_down()
        return root[1]

    def _sort_down(self):
        idx = 0
        while 2*idx + 1 < len(self.pqueue):
            if 2*idx + 2 == len(self.pqueue):
                comp_idx = 2*idx + 1
            else:
                if self.pqueue[2*idx + 1][0] > self.pqueue[2*idx + 2][0]:
                    comp_idx = 2*idx + 1
                else:
                    comp_idx = 2*idx + 2
            if self.pqueue[comp_idx][0] > self.pqueue[idx][0]:
                temp_parent = self.pqueue[idx]
                self.pqueue[idx] = self.pqueue[comp_idx]
                temp_parent = self.pqueue[comp_idx]
                self.pqueue[comp_idx] = self.pqueue[idx]
            idx = comp_idx

    def peek(self):
        return self.pqueue[0]

