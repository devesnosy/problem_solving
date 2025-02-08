# https://codeforces.com/problemset/problem/158/A

n, k = map(int, input().split())

# Convert to zero indexing
k -= 1

scores = list(map(int, input().split()))

kth_score = scores[k]

nwinners = 0

for s in scores:
    if s == 0:
        break
    if s >= kth_score:
        nwinners += 1
    else:
        break

print(nwinners)
