"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/6321
"""

import sys

for i in range(int(sys.stdin.readline())):
    name = sys.stdin.readline()
    computer = ""
    for j in range(len(name)-1):
        if name[j] == 'Z':
            computer += 'A'
        else:
            computer += chr(ord(name[j])+1)
    print("String #", i+1, sep='')
    print(computer)
    print()
