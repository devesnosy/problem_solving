# https://codeforces.com/problemset/problem/144/A

n = int(input())

a = [int(s) for s in input().split()]
max_i = len(a) - 1
i = len(a) - 2

# Target is to swap max element with all its neighbours until it becomes the first
# so we scan backwards in case of multiple max elements we choose the one closer to first
# so that we minimuze number of swaps
while i >= 0:
    if a[i] >= a[max_i]:
        max_i = i
    i -= 1

# Similar logic for min element, it needs to become last, so we choose the minimum element that is closest to last position
# so we scan from first to last
# so later minimum elements will override the recorded index for minimum element
min_i = 0
i = 1
while i < len(a):
    if a[i] <= a[min_i]:
        min_i = i
    i += 1

# number of needed swap between two indices = abs(i1 - i2)

n_swaps_for_max = max_i
n_swaps_for_min = len(a) - 1 - min_i

n_needed_swaps = n_swaps_for_max + n_swaps_for_min

# Special case when max_i is greater than min_i
# the one of the max swaps will move the min elem closer to last
# so we subtract one
if max_i > min_i:
    n_needed_swaps -= 1

print(n_needed_swaps)
