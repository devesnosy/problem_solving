# https://codeforces.com/problemset/problem/58/A

target = "hello"

s = input()

ti = 0

for c in s:
    if c == target[ti]:
        ti += 1
    if ti == len(target):
        print("YES")
        exit()
print("NO")
