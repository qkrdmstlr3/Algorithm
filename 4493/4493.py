"""
    Author : ParkEunsik
    Date   : 2019/09/20
    url    : https://www.acmicpc.net/problem/4493
"""

import sys

num = [['R', 'R'], ['S', 'S'], ['P', 'P'], ['R', 'P'], ['S', 'R'], ['P', 'S'], ['R', 'S'], ['S', 'P'], ['P', 'R']]
for _ in range(int(sys.stdin.readline())):
    count = 0
    for _ in range(int(sys.stdin.readline())):
        array = sys.stdin.readline().split()
        if num.index(array) <= 2:
            continue
        elif num.index(array) <= 5:
            count -= 1
        else:
            count += 1
    if count == 0:
        print("TIE")
    elif count > 0:
        print("Player 1")
    else:
        print("Player 2")
