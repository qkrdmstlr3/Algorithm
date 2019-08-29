"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/5054
"""

import sys

for i in range(int(sys.stdin.readline())):
    N = sys.stdin.readline()
    store = sorted(list(map(int, sys.stdin.readline().split())))
    print(2*(store[-1]-store[0]))
    
