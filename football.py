# https://codeforces.com/problemset/problem/96/A

s = input()

nconsec = 1

curr = s[0]
for c in s[1:]:
    if c == curr:
        nconsec += 1
    else:
        curr = c
        nconsec = 1
    if nconsec == 7:
        print("YES")
        exit()

print("NO")
