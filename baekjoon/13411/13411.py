"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13411
    correct percentage : 39.583%
"""

import sys
import math
from operator import itemgetter

array = []
for i in range(int(sys.stdin.readline())):
    x, y, speed = map(int, sys.stdin.readline().split())
    distance = math.sqrt((x**2)+(y**2))
    array.append([i+1, distance/speed])
array.sort(key = itemgetter(1, 0))
for i in array:
    print(i[0])
