"""
    Author : ParkEunsik
    Date   : 2019/07/29
    url    : https://www.acmicpc.net/problem/10769
"""

import sys

text = input()
happy, sad = 0, 0
for i in range(len(text)-2):
    if text[i] == ':' and text[i+1] == '-' and text[i+2] == ')':
        happy += 1
    elif text[i] == ':' and text[i+1] == '-' and text[i+2] == '(':
        sad += 1
if happy == 0 and sad == 0:
    print("none")
elif happy == sad:
    print("unsure")
elif happy > sad:
    print("happy")
else:
    print("sad")
