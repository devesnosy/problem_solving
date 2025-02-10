# https://codeforces.com/problemset/problem/427/A

n = int(input())

n_officers = 0
n_untreated_crimes = 0
for e in (int(s) for s in input().split()):
    if e == -1:
        if n_officers == 0:
            n_untreated_crimes += 1
        else:
            n_officers -=1
    else:
        n_officers += e

print(n_untreated_crimes)
