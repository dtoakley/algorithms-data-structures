
class HashMap(object):

    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def __setitem__(self, key, data):
        self.put(key, data)

    def __getitem__(self, key):
        return self.get(key)

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def rehash(old_hash, size):
        return (old_hash + 1) % size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data  # replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] is not key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data  # replace

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data


# key terms
# load factor (λ) = ratio of used slots / table size
# perfect hash function = a hash function that maps each item into a unique slot without collision
# folding method = a hash function that divides an item into equal size pieces and adds them before getting  the modulo.
# mid square method = a hash f(), item is squared, then some portion (e.g. middle 2 numbers) is used to get the modulo
# collision resolution = the process for finding a hash slot when two items have the same hash value
# open addressing/rehashing = process by which you start at the original hash value, and search for the first open slot
# linear probing = systematically visiting each slot at a time looking for an empty slot for the value
# clustering = the tendency for linear probing to cause items to gather around common has values.
# quadratic probing = instead of a constant "skip" value, rehash function that increments the hash value by 1, 3, 5..
# chaining = allowing many items to exist on the same slot via references to each other. Makes searching harder.

# example hash functions


def simple_hash(num, table_size):
    return num % table_size


def ord_hash(string, table_size):
    sum = 0
    for pos in range(len(string)):
        sum = sum + ord(string[pos])

    return sum % table_size


def ord_hash_weighted(string, table_size):
    sum = 0
    for pos in range(len(string)):
        weight = pos + 1
        sum = sum + (ord(string[pos]) * weight)

    return sum % table_size

print(ord_hash('cat', 11))
print(ord_hash_weighted('cat', 11))