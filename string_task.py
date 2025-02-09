# https://codeforces.com/problemset/problem/118/A

vowels = "aoyeui"

s = input().lower()
result = "" # not best perf but ok

for c in s:
    if not (c in vowels):
        result = result + "." + c

print(result)
