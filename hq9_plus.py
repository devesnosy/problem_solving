# https://codeforces.com/problemset/problem/133/A

instructions_with_output = "HQ9"

p = input()

for c in p:
    if c in instructions_with_output:
        print("YES")
        break
else:
    print("NO")
