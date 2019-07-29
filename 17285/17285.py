"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/17285
    A ^ B = C
    A ^ C = B
    B ^ C = A
"""

import sys

T = input()
key = ord('C') ^ ord(T[0])
for i in range(len(T)):
    print(chr(ord(T[i]) ^ key), end='')
