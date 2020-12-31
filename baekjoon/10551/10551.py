"""
    Author : ParkEunsik
    Date   : 2019/07/31
    url    : https://www.acmicpc.net/problem/10551
"""

import sys


def count(t):
    if t == '1' or t == 'Q' or t == 'A' or t == 'Z':
        return 0
    elif t == '2' or t == 'W' or t == 'S' or t == 'X':
        return 1
    elif t == '3' or t == 'E' or t == 'D' or t == 'C':
        return 2
    elif t == '4' or t == 'R' or t == 'F' or t == 'V' or t == '5' or t == 'T' or t == 'G' or t == 'B':
        return 3
    elif t == '6' or t == 'Y' or t == 'H' or t == 'N' or t == '7' or t == 'U' or t == 'J' or t == 'M':
        return 4
    elif t == '8' or t == 'I' or t == 'K' or t == ',':
        return 5
    elif t == '9' or t == 'O' or t == 'L' or t == '.':
        return 6
    elif t == '0' or t == '-' or t == '=' or t == 'P' or t == '[' or t == ']' or t == ';' or t == '\'' or t == '/':
        return 7


finger_count = [0]*8
text = sys.stdin.readline()
for i in range(len(text)-1):
    finger_count[count(text[i])] += 1
for i in range(len(finger_count)):
    print(finger_count[i])
