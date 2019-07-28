"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/17363
"""

import sys


def switch(text):
    return {'.': '.', 'O': 'O', '-': '|', '|': '-', '/': '\\', '\\': '/', '^': '<', '<': 'v', 'v': '>', '>': '^'}[text]


pic = []
row, column = map(int, sys.stdin.readline().split())
for i in range(row):
    pic.append(sys.stdin.readline())

for i in reversed(range(column)):
    for j in range(row):
        print(switch(pic[j][i]), end='')
    print()
