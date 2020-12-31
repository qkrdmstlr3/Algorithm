"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13412
"""

import sys
import math
from fractions import gcd

for _ in range(int(sys.stdin.readline())):
    count = 0
    n = int(sys.stdin.readline())
    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0 and gcd(n//i, i) == 1:
            count += 1
    print(count)
        