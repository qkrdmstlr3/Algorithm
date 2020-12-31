"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2754
    correct percentage : 33.688%
"""

import sys


def switch(num):
    return {'A+':4.3, 'A0':4.0, 'A-':3.7, 'B+':3.3, 'B0':3.0, 'B-':2.7, 'C+':2.3, 'C0':2.0, 'C-':1.7, 'D+':1.3, 'D0':1.0, 'D-':0.7, 'F':0.0}[num]


print(switch(input()))
