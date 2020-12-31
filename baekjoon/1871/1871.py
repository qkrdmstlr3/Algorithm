"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/1871
"""

import sys

for i in range(int(sys.stdin.readline())):
    text, num = sys.stdin.readline().split('-')
    price = abs(int(num) - (676*(ord(text[0])-65) + 26*(ord(text[1])-65) + ord(text[2])-65))
    if price <= 100:
        print("nice")
    else:
        print("not nice")
