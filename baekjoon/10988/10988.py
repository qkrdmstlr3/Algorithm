"""
    Author : ParkEunsik
    Date   : 2019/07/28
    url    : https://www.acmicpc.net/problem/10988
"""

import sys

text = input()

for i in range(len(text)//2):
    if text[i] != text[-i-1]:
        print(0)
        exit()
print(1)
