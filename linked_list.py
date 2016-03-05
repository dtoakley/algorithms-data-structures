
class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        new_node = Node(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        prev = None
        found = False

        while not found:
            if current.get_data == item:
                found = True
            else:
                prev = current
                current = current.get_next()

        if prev is None:
            self.head == current.get_next()
        else:
            prev.set_next(current.get_next())

    def append(self, item):
        current = self.head
        end_item = False
        new_node = Node(item)

        while not end_item:
            if current.get_next() is None:
                end_item = True
                current.set_next(new_node)
            else:
                current = current.get_next()

my_list = UnorderedList()
my_list.add(4)
my_list.add(9)
my_list.add("asd")
my_list.append("appended item")

# print(my_list.search(9))
print(my_list.size())


class OrderedList(object):

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False
        stop = False

        while current is not None and not found and not stop :
            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.get_next()

        return found

    def add(self, item):
        current = self.head
        prev = None
        stop = False

        while current is not None and not stop:
            if current.get_data() > item:
                stop = True
            else:
                current = current.get_next()
                prev = current

        new_item = Node(item)

        if current == self.head:
            self.head = new_item
            new_item.set_next(current)
        else:
            prev.set_next(new_item)
            new_item.set_next(current)
