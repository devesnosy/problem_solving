# https://codeforces.com/problemset/problem/705/A

n = int(input())

print("I hate", end="")
for i in range(2, n + 1):
    print(" that ", end="")
    if i % 2 == 0:
        print("I love", end="")
    else:
        print("I hate", end="")

print(" it")
