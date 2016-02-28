
class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def hot_potato(name_list, num):
    queue = Queue()

    for name in name_list:
        queue.enqueue(name)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"], 7))
