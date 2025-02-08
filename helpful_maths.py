# https://codeforces.com/problemset/problem/339/A

nums = list(map(int, input().split("+")))
nums.sort()
print("+".join(map(str, nums)))
