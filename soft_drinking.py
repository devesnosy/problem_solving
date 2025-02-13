# https://codeforces.com/problemset/problem/151/A

n, k, l, c, d, p, nl, np = map(int, input().split())

total_l = k * l
total_slices = c * d

num_slices_per_friend = total_slices // n
l_per_friend = total_l // n
grams_of_salt_per_friend = p // n

num_toasts = min(num_slices_per_friend, l_per_friend // nl, grams_of_salt_per_friend // np)

print(num_toasts)
