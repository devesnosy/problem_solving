# https://codeforces.com/problemset/problem/318/A

n, k = map(int, input().split())

neven = n // 2
nodd = n - neven

k -= 1 # Convert to zero index

# odds are listed first, if index is greater than then we need to get an even number
if k > (nodd - 1):
    k -= nodd
    print(2 * (k + 1))
else:
    print(2 * (k + 1) - 1)
