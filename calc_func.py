# https://codeforces.com/problemset/problem/486/A

n = int(input())

def arithmetic_sum(a, d, n):
    return (n * (2 * a + (n - 1) * d)) // 2

num_even = n // 2
num_odd = n - num_even
result = arithmetic_sum(2, 2, num_even) - arithmetic_sum(1, 2, num_odd)

print(result)
