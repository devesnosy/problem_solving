# https://codeforces.com/problemset/problem/230/B

from math import sqrt

n = int(input())
for x in map(int, input().split()):
    if x == 1:
        print("NO")
        continue
    root = sqrt(x)
    if root % 1 == 0:
        # Number is square, check if root is prime
        pd = 2
        while pd * pd <= root:
            if root % pd == 0:
                print("NO")
                break
            pd += 1
        else:
            print("YES")
    else:
        print("NO")
    # num_unique_divisors = 0
    # pd = 1
    # while pd * pd <= x:
    #     xod, xmd = divmod(x, pd)
    #     if xmd == 0:
    #         if xod == pd:
    #             num_unique_divisors += 1
    #         else:
    #             num_unique_divisors += 2
    #     pd += 1
    # print("YES" if (num_unique_divisors == 3) else "NO")
