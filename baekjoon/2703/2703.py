"""
    Author : ParkEunsik
    Date   : 2019/09/20
    url    : https://www.acmicpc.net/problem/2703
"""

import sys

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for _ in range(int(sys.stdin.readline())):
    message = list(sys.stdin.readline().rstrip())
    pattern = list(sys.stdin.readline().rstrip())
    
    for i in range(len(message)):
        if message[i] == ' ':
            continue
        message[i] = pattern[alphabet.index(message[i])]
    print(''.join(message))
