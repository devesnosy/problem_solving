# https://codeforces.com/problemset/problem/492/B

n, l = map(int, input().split())

# No need to deduplicate since we are keeping track of max consecutive diff anyways
# so duplicate items will result in diff of zero and won't affect max consecutive diff
lantern_locations = [int(s) for s in input().split()]
lantern_locations = sorted(lantern_locations)

a_iter = iter(lantern_locations)

prev = next(a_iter)

#d: diff
max_d = 0

for a in a_iter:
    d = a - prev
    if d > max_d:
        max_d = d
    prev = a

possible_min_needed_distance = max_d / 2

# Handle edges
min_needed_d = possible_min_needed_distance;
if (l - lantern_locations[-1]) > min_needed_d:
    min_needed_d = l - lantern_locations[-1]

if (lantern_locations[0] - 0) > min_needed_d:
    min_needed_d = lantern_locations[0] - 0

print(min_needed_d)
