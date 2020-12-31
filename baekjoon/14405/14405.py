"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/14405
    correct percentage : 50.378%
"""

import sys

text = sys.stdin.readline().rstrip()
length = len(text)

replace = text.replace('pi','')
length -= len(text)-len(replace)

replace = text.replace('ka','')
length -= len(text)-len(replace)

replace = text.replace('chu','')
length -= len(text)-len(replace)

if length == 0:
    print("YES")
else:
    print("NO")
