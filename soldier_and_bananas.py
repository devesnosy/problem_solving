# https://codeforces.com/problemset/problem/546/A

k, n, w = map(int, input().split())

# Sum of arithmetic series
total = (w * (k + w * k)) // 2

print(total - n)
