# https://codeforces.com/problemset/problem/723/A

xs = [int(s) for s in input().split()]

xs.sort()

# Total distance from other nodes to median
# "The distance between the median and the remaining values is less than any other point's distance.""
print(xs[1] - xs[0] + xs[2] - xs[1])
