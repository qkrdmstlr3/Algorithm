"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/13420
"""

import sys

for i in range(int(sys.stdin.readline())):
    first, operator, second, equal ,result = sys.stdin.readline().split(' ')
    if operator == '+':
        if int(first) + int(second) == int(result):
            print("correct")
        else:
            print("wrong answer")
    elif operator == '-':
        if int(first) - int(second) == int(result):
            print("correct")
        else:
            print("wrong answer")
    elif operator == '*':
        if int(first) * int(second) == int(result):
            print("correct")
        else:
            print("wrong answer")
    elif operator == '/':
        if int(first) // int(second) == int(result):
            print("correct")
        else:
            print("wrong answer")
