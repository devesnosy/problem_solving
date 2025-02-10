# https://codeforces.com/problemset/problem/479/A

a, b, c = (int(input()) for _ in range(3))

print(max(
    (a + b) * c,
    a * (b + c),
    a * b * c,
    a + b + c
),
)
