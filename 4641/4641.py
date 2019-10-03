"""
    Author : ParkEunsik
    Date   : 2019/10/03
    url    : https://www.acmicpc.net/problem/4641
"""

import sys

while True:
    num = sorted(list(map(int, sys.stdin.readline().split())))
    count = 0
    if num[0] == -1:
        break
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[i]*2 == num[j]:
                count += 1
                break
    print(count)
            
