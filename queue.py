from random import randrange


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


class Printer(object):

    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task is not None:
            return True
        else:
            return False

    def start_next(self, new_task):
        self.current_task = new_task
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate


class Task(object):

    def __init__(self, time):
        self.timestamp = time
        self.pages = randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def new_print_task():
    num = randrange(1,181)
    if num == 180:
        return True
    else:
        return False


def printer_simulation(num_seconds, pages_per_minute):

    printer = Printer(pages_per_minute)
    queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            queue.enqueue(task)

        if (not printer.busy()) and (not queue.is_empty()):
            next_task = queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            printer.start_next(next_task)

        printer.tick()

    average_wait = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d tasks remaining." % (average_wait, queue.size()))

for i in range(10):
    printer_simulation(3600, 10)



