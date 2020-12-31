"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2942
    correct percentage : 37.141%
"""

import sys
from fractions import gcd
import math

R, G = map(int, sys.stdin.readline().split())
num = gcd(R, G)
li = []

for i in range(1, int(math.sqrt(num))+1):
    if num % i == 0:
        if num // i == i:  # 36일때 6같은수
            print(i, R//i, G//i)
        else:  # 반대편에 대칭이 되는 수 같이 넣음
            print(i, R//i, G//i)
            print((num//i), R//(num//i), G//(num//i))
            li.append(num//i)
