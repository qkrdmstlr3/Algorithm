"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/17350
"""

import sys

name = []
for i in range(int(sys.stdin.readline())):
    name.append(sys.stdin.readline())
if 'anj\n' in name:
    print("뭐야;")
else:
    print("뭐야?")
