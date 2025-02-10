# https://codeforces.com/problemset/problem/996/A

n = int(input())

bills = [100, 20, 10, 5, 1]

s = 0
for b in sorted(bills, reverse=True):
    nob, nmb = divmod(n, b)
    s += nob
    n = nmb

print(s)

# n100 = n // 100

# r = n - n100 * 100

# n20 = r // 20

# r = r - n20 * 20

# n10 = r // 10

# r = r - n10 * 10

# n5 = r // 5

# r = r - n5 * 5

# n1 = r

# print(n1 + n5 + n10 + n20 + n100)
