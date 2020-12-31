"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/2857
    correct percentage : 48.365%
"""

import sys

flag = True
for i in range(5):
    agent = sys.stdin.readline()
    if 'FBI' in agent:
        print(i+1, end=' ')
        flag = False
if flag:
    print("HE GOT AWAY!")
