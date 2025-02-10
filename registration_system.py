# https://codeforces.com/problemset/problem/4/C


n = int(input())

db = dict()

for _ in range(n):
    req = input()
    if req in db:
        print(req, db[req], sep="")
        db[req] += 1
    else:
        db[req] = 1
        print("OK")
