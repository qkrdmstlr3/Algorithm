"""
    Author : ParkEunsik
    Date   : 2019/08/03
    url    : https://www.acmicpc.net/problem/10984
"""
import sys

for i in range(int(sys.stdin.readline())):
    grade, gpa = 0, 0
    for j in range(int(sys.stdin.readline())):
        c, g = map(float, sys.stdin.readline().split())
        grade += int(c)
        gpa += c*g
    gpa = '{:0.1f}'.format(gpa/grade)
    print(grade, gpa)
