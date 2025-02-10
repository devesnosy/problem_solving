# https://codeforces.com/problemset/problem/61/A

a = input()
b = input()

for ai, bi in zip(a, b):
    if ai != bi:
        print("1", end="")
    else:
        print("0", end="")

print("\n", sep="", end="")
