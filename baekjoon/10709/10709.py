"""
    Author : ParkEunsik
    Date   : 2019/08/02
    url    : https://www.acmicpc.net/problem/10709
"""

import sys

h, w = map(int, sys.stdin.readline().split())
result_list = []
for i in range(h):
    cloud = list(sys.stdin.readline())
    if 'c' not in cloud:
        result_list.append(['-1 '*w])
        continue
    else:
        add_list = []
        cloud_place = -1
        for j in range(w):
            if cloud[j] == 'c':
                add_list.append('0')
                cloud_place = 0
            elif cloud_place == -1:
                add_list.append('-1')
            elif cloud[j] == '.':
                add_list.append(str(cloud_place+1))
                cloud_place += 1
        result_list.append(add_list)
for i in range(h):
    print(' '.join(result_list[i]))
