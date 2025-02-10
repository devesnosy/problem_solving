# https://codeforces.com/problemset/problem/580/A

n = int(input())

nums = [int(s) for s in input().split()]

ws = 0 # Window start
l = 1
max_l = 1

while (ws + l) < n:
   if nums[ws + l] >= nums[ws + l - 1]:
       l += 1
       max_l = max(max_l, l)
   else:
       ws = ws + l
       l = 1

print(max_l)
