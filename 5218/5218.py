"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/5218
"""

import sys

for i in range(int(sys.stdin.readline())):
    first, second = sys.stdin.readline().split(' ')
    result = []
    for i in range(len(first)):
        if first[i] <= second[i]:
            result.append(ord(second[i])-ord(first[i]))
        else:
            result.append(ord(second[i])+26-ord(first[i]))
    print("Distances:", ' '.join(map(str, result)))
