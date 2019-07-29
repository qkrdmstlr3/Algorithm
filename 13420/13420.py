"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/13420
"""

import sys

for i in range(int(sys.stdin.readline())):
    front, end = sys.stdin.readline().split('=')
    flag = True
    end = int(end)
    if '*' in front:
        num1, num2 = map(int, front.split('*'))
        if num1*num2 != end:
            flag = False
    elif '+' in front:
        num1, num2 = map(int, front.split('+'))
        if num1+num2 != end:
            flag = False
    elif '-' in front:
        num1, num2 = map(int, front.split('-'))
        if num1-num2 != end:
            flag = False
    elif '/' in front:
        num1, num2 = map(int, front.split('/'))
        if num1//num2 != end:
            flag = False
    if flag is True:
        print("correct")
    else:
        print("wrong answer")
