# https://codeforces.com/problemset/problem/268/A

n = int(input())

uniforms = [input().split() for _ in range(n)]

# We can make it more efficient by computing length of
# intersection of host uniforms set and gues uniforms set
answer = 0
for host_i in range(n):
    for guest_i in range(n):
        if host_i == guest_i:
            continue
        hhu = uniforms[host_i][0]
        ggu = uniforms[guest_i][1]
        if hhu == ggu:
            answer += 1

print(answer)
