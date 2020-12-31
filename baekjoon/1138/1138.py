"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1138
"""

import sys

N = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))
final_line = []

for i in reversed(range(len(line))):
    final_line.insert(line[i], i+1)
print(' '.join(map(str, final_line)))
