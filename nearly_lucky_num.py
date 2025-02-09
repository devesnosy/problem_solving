# https://codeforces.com/problemset/problem/110/A

lucky_digits = "47"

s = input()

n_lucky = 0

for c in s:
    if c in lucky_digits:
        n_lucky += 1

for c in str(n_lucky):
    if not(c in lucky_digits):
        print("NO")
        exit()

print("YES")
