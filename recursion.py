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

# t0 = time.clock()
# result = fib_brute(n)
# t1 = time.clock()
# print("fib brute({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))
#
# t0 = time.clock()
# result = fib_recursive(n)
# t1 = time.clock()
# print("fib recursive({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))
#
# t0 = time.clock()
# result = fib_memo(n)
# t1 = time.clock()
# print("fib recursive({0}) = {1}, ({2:.2f} secs)".format(n, result, t1-t0))


def toStr(num, base):
    convertString = '0123456789ABCDEF'
    if num < base:
        return convertString[num]
    else:
        return toStr(num // base, base) + convertString[num % base]

print(toStr(3446, 10))


def reverseStr(string):
    if len(string) == 1:
        return string
    else:
        return reverseStr(string[1:]) + string[0]

print(reverseStr("follow"))


def isPalindrome(string):
    string = string.replace(" ", "").lower()
    if len(string) <= 1:
        return True
    if string[0] != string[-1]:
        return False
    else:
        return isPalindrome(string[1:-1])

print(isPalindrome("Live not on evil"))


def move_disk(from_pole, to_pole):
    print('moving disk from ', from_pole, 'to', to_pole)


def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)

move_tower(3, "A", "B", "C")


def memo_fewest_coins(coin_list, change, known_results):
    min_coins = change
    if change in coin_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_list if c <= change]:
            num_coins = 1 + memo_fewest_coins(coin_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins
    return min_coins

print(memo_fewest_coins([1, 5, 10, 25], 63, [0]*64))


def dynamic_fewest_coins(coin_list, change, min_coins, coins_used):
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        for j in [c for c in coin_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
            min_coins[cents] = coin_count
            coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin -= this_coin


def fewest_coins_main():
    amount = 63
    coin_list = [1, 5, 10, 20, 25]
    coins_used = [0]*(amount+1)
    coin_count = [0]*(amount+1)

    print("Making change for",amount,"requires")
    print(dynamic_fewest_coins(coin_list, amount, coin_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used,amount)
    print("The used list is as follows:")
    print(coins_used)

fewest_coins_main()