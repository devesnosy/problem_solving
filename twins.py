# https://codeforces.com/problemset/problem/160/A

_ = input()
coins = [int(s) for s in input().split()]
coins_sum = sum(coins)
coins.sort(reverse=True) # Take larger coins first to minimize number of taken coins

n = 0
taken_sum = 0
for c in coins:
    taken_sum += c
    n += 1
    if taken_sum > (coins_sum - taken_sum):
        break

print(n)
