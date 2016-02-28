
class Deque():

    def __init__(self):
        self.items = []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


def palindrome_checker(string):
    deque = Deque()

    for char in string:
        deque.add_rear(char)

    still_equal = True

    while deque.size() > 1 and still_equal:
        first = deque.remove_front()
        last = deque.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("radar"))
