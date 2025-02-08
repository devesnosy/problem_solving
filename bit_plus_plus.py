# https://codeforces.com/problemset/problem/282/A

x = 0

n = int(input())

for _ in range(n):
    statement = input()
    if "-" in statement:
        x -= 1
    elif "+" in statement:
        x += 1

print(x)
