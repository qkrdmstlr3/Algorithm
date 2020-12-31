"""
    Author : ParkEunsik
    Date   : 2019/10/01
    url    : https://www.acmicpc.net/problem/11655
"""

import sys

text = list(sys.stdin.readline().rstrip())
for i in range(len(text)):
    if 90 >= ord(text[i]) >= 65: 
        if ord(text[i])+13 > 90:
            text[i] = chr(65 + ord(text[i])+13 - 91)
        else:
            text[i] = chr(ord(text[i])+13)
    elif 122 >= ord(text[i]) >= 97:
        if ord(text[i])+13 > 122:
            text[i] = chr(97 + ord(text[i])+13 - 123)
        else:
            text[i] = chr(ord(text[i])+13)
print(''.join(text))
