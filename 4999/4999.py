"""
    Author : ParkEunsik
    Date   : 2019/08/29
    url    : https://www.acmicpc.net/problem/4999
"""

import sys

person = input()
doctor = input()
if len(person) >= len(doctor):
    print("go")
else:
    print("no")
