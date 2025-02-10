# https://codeforces.com/problemset/problem/405/A

_ = input()

# First row will be always full since number of cubes is always greater than 1 per the problem statement
# I just realized sorting will produce needed result
columns = [int(s) for s in input().split()]
columns.sort()

print(*columns)
