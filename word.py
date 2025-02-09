# https://codeforces.com/problemset/problem/59/A

s = input()

nupper = 0
nlower = 0

for c in s:
    if c.isupper():
        nupper += 1
    else:
        nlower += 1

if nupper > nlower:
    print(s.upper())
else:
    print(s.lower())
