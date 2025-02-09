# https://codeforces.com/problemset/problem/266/A

n = int(input())

s = input()

answer = 0

i = 0

current = s[i]
i+= 1

while i < len(s):
    if current == s[i]:
        answer += 1
    else:
        current = s[i]
    i += 1

print(answer)
