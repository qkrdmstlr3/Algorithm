"""
    Author : ParkEunsik
    Date   : 2019/07/22
    url    : https://www.acmicpc.net/problem/1654
"""

import sys


def l_sum(l, m):
    s = 0
    for i in range(len(l)):
        s += l[i] // m
    return s


K, N = map(int, sys.stdin.readline().split())
lan = []

for i in range(K):
    lan.append(int(sys.stdin.readline()))
mx_l, mi_l = max(lan), 0
mid = (mx_l+mi_l)//2
while 0:
    cnt = l_sum(lan, mid)
    if cnt < N:
        mx_l = mid
        mid = (mx_l+mi_l)//2
    elif cnt > N:
        mi_l = mid
        mid = (mx_l+mi_l)//2
    elif cnt == N:
        if cnt == l_sum(lan, mid+1):
            mi_l = mid
            mid = (mx_l+mi_l)//2
        else:
            break
print(mid)
