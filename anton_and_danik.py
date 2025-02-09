# https://codeforces.com/problemset/problem/734/A

n = int(input())

na = 0
nd = 0

s = input()

for c in s:
    if c == "A":
        na += 1
    else:
        nd += 1

if na == nd:
    print("Friendship")
elif na > nd:
    print("Anton")
else:
    print("Danik")
