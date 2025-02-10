# https://codeforces.com/problemset/problem/510/A

n, m = map(int, input().split())

alt = False
for r in range(n):
    if r % 2 == 0:
        print("#" * m)
    else:
        if alt:
            print("#" + (m - 1) * ".")
        else:
            print("." * (m - 1) + "#")
        alt = not alt
