# https://codeforces.com/problemset/problem/520/A

import string

alphabet = set(string.ascii_lowercase)

_ = input()
s = input().lower()

print("YES" if set(s) == alphabet else "NO")
