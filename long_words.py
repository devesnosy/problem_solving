# https://codeforces.com/contest/71/problem/A

n = int(input())

for _ in range(n):
    word = input()
    l = len(word)
    if l > 10:
        print(word[0] + f"{l - 2}" + word[-1])
    else:
        print(word)
