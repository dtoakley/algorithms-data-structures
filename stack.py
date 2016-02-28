
class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        self.items.append(item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[-1]


def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in '([{':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False
        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


def matches(open, close):
    openers = '([{'
    closers = ')]}'
    return openers.index(open) == closers.index(close)


print(par_checker('{{([][])}()}'))
print(par_checker('[{()]'))


def base_converter(dec_num, base):
    digits = "0123456789ABCDEF"
    stack = Stack()

    while dec_num > 0:
        rem = dec_num % base
        stack.push(rem)
        dec_num = dec_num // base

    binary_string = ""
    while not stack.is_empty():
        binary_string += digits[stack.pop()]

    return binary_string

print(base_converter(25, 2))
print(base_converter(26, 26))

