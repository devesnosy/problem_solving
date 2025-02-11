def odd_num_index(odd_num):
    # assert odd_num > 0
    # assert odd_num % 2 == 1, odd_num
    return (odd_num + 1) // 2 - 1

def ith_odd(i):
    # assert i > 0
    return 2 * (i + 1) - 1

def num_odd_nums_le_n(n):
    return n - n // 2

n = 120

is_prime_arr = [True] * (num_odd_nums_le_n(n) - 1)

# p: prime
# c: composite
p = 3
while p * p <= n:
    if is_prime_arr[odd_num_index(p) - 1]:
        c = p * p
        while c <= n:
            if c % 2 == 1:
                is_prime_arr[odd_num_index(c) - 1] = False
            c += p
    p += 2

for i, is_prime in enumerate(is_prime_arr):
    if is_prime:
        print(ith_odd(i + 1))
