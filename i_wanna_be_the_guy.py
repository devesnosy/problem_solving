# https://codeforces.com/problemset/problem/469/A

n = int(input())
_, *x_levels = map(int, input().split())
_, *y_levels = map(int, input().split())

can_they_win = len(set(x_levels + y_levels)) == n

if can_they_win:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
