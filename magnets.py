# https://codeforces.com/problemset/problem/344/A

n = int(input())

current_pole = input()

num_groups = 1

for _ in range(n - 1):
    pole = input()
    if pole != current_pole:
        num_groups += 1
        current_pole = pole

print(num_groups)
