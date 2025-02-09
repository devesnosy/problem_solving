# https://codeforces.com/problemset/problem/617/A

x = int(input())

# We try to take as many steps as possible
# once we take all steps in 5 units,
# we try to take in 4 and so one
# the math works out in the end

# we could generalize this with a recursive function I guess
# r stands for remainder or remaining

n5 = x // 5

r = x - n5 * 5

n4 = r // 4

r = r - n4 * 4

n3 = r // 3

r = r - n3 * 3

n2 = r // 2

r = r - n2 * 2

n1 = r // 1

print(n5 + n4 + n3 + n2 + n1)
