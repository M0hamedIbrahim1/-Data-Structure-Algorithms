# link    : https://codeforces.com/contest/1850/problem/E
 # author : Mohamed Ibrahim
def solve():
    n, c = map(int, input().split())
    a = list(map(int, input().split()))
    l, r = 1, 10**9
    while l <= r:
        mid = l + (r - l) // 2
        sumall = 0
        for i in range(n):
            sumall += (a[i] + 2 * mid)**2
            if sumall > c:
                break
        if sumall == c:
            print(mid)
            return
        elif sumall > c:
            r = mid - 1
        else:
            l = mid + 1
 
for _ in range(int(input())):
    solve()
