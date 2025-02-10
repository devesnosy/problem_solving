# https://codeforces.com/problemset/problem/158/B

n = int(input())

# Keep track of how many gorups of ones and how many groups of twos and so on
group_size_counter = [0] * 4

for s in map(int, input().split()):
    group_size_counter[s - 1] += 1



res = 0

res += group_size_counter[3]

group_size_counter[3] = 0

num_3_plus_1_groups = min(group_size_counter[0], group_size_counter[2])

res += num_3_plus_1_groups

group_size_counter[0] -= num_3_plus_1_groups
group_size_counter[2] -= num_3_plus_1_groups

num_2_plus_2_groups = group_size_counter[1] // 2

res += num_2_plus_2_groups

group_size_counter[1] -= num_2_plus_2_groups * 2


num_double_one_groups = group_size_counter[0] // 2
num_2_plus_double_groups = min(num_double_one_groups, group_size_counter[1])

res += num_2_plus_double_groups

group_size_counter[0] -= num_2_plus_double_groups * 2
group_size_counter[1] -= num_2_plus_double_groups

num_quad_one_groups = group_size_counter[0] // 4

res += num_quad_one_groups

group_size_counter[0] -= num_quad_one_groups * 4


num_2_plus_one_groups = min(group_size_counter[0], group_size_counter[1])

res += num_2_plus_one_groups

group_size_counter[0] -= num_2_plus_one_groups
group_size_counter[1] -= num_2_plus_one_groups

if group_size_counter[0] > 0:
    res += 1

if group_size_counter[1] > 0:
    res += 1

if group_size_counter[2] > 0:
    res += group_size_counter[2]

group_size_counter = [0] * 4 # not needed, just to illustrate


print(res)
