from collections import Counter

g = input()
h = input()
p = input()

if Counter(g + h) == Counter(p):
    print("YES")
else:
    print("NO")
