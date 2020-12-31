"""
    Author : ParkEunsik
    Date   : 2019/10/01
    url    : https://www.acmicpc.net/problem/12174
"""

import sys

for m in range(int(sys.stdin.readline())):
    b = int(sys.stdin.readline());
    text = list(sys.stdin.readline().rstrip())
    result = []
    for i in range(0, len(text), 8):
        num = ''
        for j in range(i, i+8):
            if text[j] == 'O':
                num += '0'
            else:
                num += '1'
        num = int(num, 2)
        result.append(chr(num))
    print("Case #",m+1,": ",''.join(result), sep='')
