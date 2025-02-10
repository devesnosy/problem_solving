# https://codeforces.com/problemset/problem/443/A

# we can make it more robust but I'm dealing with bullies
# and trying to relax by solving problems
tokens = input().split()
if tokens == ["{}"]:
    print("0")
else:
    tokens[0] = tokens[0][1:]
    tokens[-1] = tokens[-1][:-1] + ","
    print(len(set(tokens)))
