# https://codeforces.com/problemset/problem/263/A

matrix = [[0] * 5] * 5

for i in range(5):
    matrix[i] = list(map(int, input().split()))


oi = 0
oj = 0
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            oi = i
            oj = j
            break

# Minimum number of row and column swaps to move 1 to center
di = abs(oi - 2)
dj = abs(oj - 2)
print(di + dj)
