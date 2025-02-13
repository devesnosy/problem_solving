# https://codeforces.com/problemset/problem/750/A
from math import sqrt, floor

def calc_discriminant(a, b, c):
    return b * b - 4 * a * c

n, k = map(int, input().split())

total_time = 4 * 60
avail_time = total_time - k


a = 5 # first item
d = 5 # difference between items
s = avail_time # arithmetic seq. sum

# q: quadratic equation
qa = d
qb = 2 * a - d
qc = -2 * s

disc = calc_discriminant(qa, qb, qc)
x = (-qb + sqrt(disc)) / (2 * qa)

x = floor(x)
if x > n:
    x = n

print(x)
