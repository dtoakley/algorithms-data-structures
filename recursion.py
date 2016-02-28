import time


def recursive_add(nested_num_list):
    total = 0

    for num in nested_num_list:
        if type(num) == type([]):
            total += recursive_add(num)
        else:
            total += num

    return total

print(recursive_add([1,4,[4,7,9,[3,4,5]]]))


def fib_brute(n):
    if n < 2:
        return n

    prev = 1
    current = 1

    for num in range(2, n):
        prev, current = current, prev + current

    return current

assert (fib_brute(0) == 0)
assert (fib_brute(6) == 8)


def fib_recursive(n):

    if n < 2:
        return n
    else:
        return fib_recursive(n - 1) + fib_recursive(n - 2)

assert (fib_recursive(0) == 0)
assert (fib_recursive(6) == 8)

alreadyknown = {0: 0, 1: 1}


def fib_memo(n):
    if n not in alreadyknown:
        new_value = fib_memo(n-1) + fib_memo(n-2)
        alreadyknown[n] = new_value
    return alreadyknown[n]

n = 35

t0 = time.clock()
result = fib_brute(n)
t1 = time.clock()
print("fib brute({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

# t0 = time.clock()
# result = fib_recursive(n)
# t1 = time.clock()
# print("fib recursive({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))

t0 = time.clock()
result = fib_memo(n)
t1 = time.clock()
print("fib recursive({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))