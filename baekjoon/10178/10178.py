"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/10178
"""

import sys

for i in range(int(sys.stdin.readline())):
    candy, brother = map(int, sys.stdin.readline().split())
    print('You get ', candy//brother, ' piece(s) and your dad gets ', candy%brother, ' piece(s).', sep='')
