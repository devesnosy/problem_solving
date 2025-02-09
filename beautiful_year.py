# https://codeforces.com/problemset/problem/271/A

y = int(input())

y += 1
while True:
    sy = str(y)
    if len(sy) == len(set(sy)):
        print(sy)
        exit()
    else:
        y += 1
