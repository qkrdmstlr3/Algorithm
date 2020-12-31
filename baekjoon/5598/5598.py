"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/5598
"""
import sys

word = sys.stdin.readline()

for i in range(len(word) - 1):
    if word[i] == 'A':
        print('X', end='')
    elif word[i] == 'B':
        print('Y', end='')
    elif word[i] == 'C':
        print('Z', end='')
    else:
        print(chr(ord(word[i])-3), end='')
