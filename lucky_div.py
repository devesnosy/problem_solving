# https://codeforces.com/problemset/problem/122/A

lucky_digits = "47"

def is_lucky(n):
    for c in str(n):
        if not ( c in lucky_digits):
            return False
    return True

def is_almost_lucky(n):
    for d in range(n, 0, -1):
        if n % d == 0 and is_lucky(d):
            return True
    return False

n = int(input())
print("YES" if is_almost_lucky(n) else "NO")
