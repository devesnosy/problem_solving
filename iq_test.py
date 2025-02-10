# https://codeforces.com/problemset/problem/25/A

n = int(input())

nums = [int(s) for s in input().split()]

def is_even(x):
    return x % 2 == 0

for i in range(n):
    prev = nums[(i - 1) % n]
    next_ = nums[(i + 1) % n]
    curr = nums[i]
    if is_even(curr) != is_even(next_) and is_even(curr) != is_even(prev):
        print(i + 1)
        break
