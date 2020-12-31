"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5988
"""

import sys

for i in range(int(sys.stdin.readline())):
    if int(sys.stdin.readline().rstrip()[-1]) % 2 == 0:
        print("even")
    else:
        print("odd")
