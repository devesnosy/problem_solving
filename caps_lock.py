# https://codeforces.com/problemset/problem/131/A

s = input()
if s.isupper() or (s[0].islower() and (s[1:].isupper() or len(s) == 1 ) ):
    print(s.swapcase())
else:
    print(s)
