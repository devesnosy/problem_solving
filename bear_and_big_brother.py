# https://codeforces.com/problemset/problem/791/A

a, b = map(int, input().split())

# Since input is small we can use a simple loop

i = 0
while a <= b:
   a *= 3
   b *= 2
   i += 1

print(i)
