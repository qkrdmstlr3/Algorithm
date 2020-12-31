"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/2966
    correct percentage : 44.485%
"""

import sys

sang = ['A', 'B', 'C']
chang = ['B', 'A', 'B', 'C']
hyun = ['C', 'C', 'A', 'A', 'B', 'B']
score = [0, 0, 0]
name = ['Adrian', 'Bruno', 'Goran']

N = int(sys.stdin.readline())
text = sys.stdin.readline().rstrip()

for i in range(len(text)):
    if text[i] == sang[i%3]:
        score[0] += 1
    if text[i] == chang[i%4]:
        score[1] += 1
    if text[i] == hyun[i%6]:
        score[2] += 1
print(max(score))
for i in range(3):
    if score[i] == max(score):
        print(name[i])
