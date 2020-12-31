"""
    Author : ParkEunsik
    Date   : 2019/07/22
    url    : https://www.acmicpc.net/problem/1966
"""

import sys

for i in range(int(sys.stdin.readline())):
    N, M = map(int, sys.stdin.readline().split())
    ipt = list(map(int, sys.stdin.readline().split()))
    cnt = 1
    while True:
        mx = max(ipt)
        if M == 0 and ipt[0] < mx:
            tmp = ipt.pop(0)
            ipt.append(tmp)
            M = len(ipt)-1
        elif ipt[0] < mx:
            tmp = ipt.pop(0)
            ipt.append(tmp)
            M -= 1
        elif ipt[0] == mx:
            if M == 0:
                print(cnt)
                break
            ipt.pop(0)
            M -= 1
            cnt += 1
