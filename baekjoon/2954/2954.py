"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2954
"""

import sys

diary = list(input())
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(2, len(diary)):
    if diary[i-2] in vowel:
        diary[i] = ''
        diary[i-1] = ''
print(''.join(diary))
