"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/9996
    correct percentage : 36.632%
"""

import sys

N = int(sys.stdin.readline())
front, back = sys.stdin.readline().rstrip().split('*')
for i in range(N):
    word = input()
    if front+back == word:
        print("DA")
    elif front != word[:len(front)]:
        print("NE")
    elif len(front)+len(back) > len(word):
        print("NE")
    elif back != word[-len(back):]:
        print("NE")
    else:
        print("DA")
