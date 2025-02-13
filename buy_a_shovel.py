# https://codeforces.com/problemset/problem/732/A

k, r = map(int, input().split())

# Because we are using modulo 10
# only n values from 1 to 9 are needed to be checked
for n in range(1, 10):
    # 0 is edge case where we do not need to use the coin worth r,
    # because we can already pay for n shovels using our unlimited supply of coins of unit 10
    if (k * n) % 10 in (r, 0):
        print(n)
        break
