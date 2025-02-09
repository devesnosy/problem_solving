# https://codeforces.com/problemset/problem/200/B

n = int(input())

result = 0

for pi in map(int, input().split()):
    result += pi / n

print(result)
