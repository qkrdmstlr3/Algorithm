"""
    Author : ParkEunsik
    Date   : 2019/08/04
    url    : https://www.acmicpc.net/problem/3035
"""
import sys

r, c, zr, zc = map(int, sys.stdin.readline().split())
newspaper = []
for i in range(r):
    newspaper.append(list(input()))
li = []
for i in range(r):
    text = ""
    for j in range(c):
        text += newspaper[i][j]*zc
    li.append(text)
for i in range(r):
    for j in range(zr):
        print(li[i])
