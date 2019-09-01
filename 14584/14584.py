"""
    Author : ParkEunsik
    Date   : 2019/09/01
    url    : https://www.acmicpc.net/problem/14593
    correct percentage : 41.834%
"""

import sys
from collections import deque

text = sys.stdin.readline().rstrip()
dictionary = []
alphabet = deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])

for i in range(int(sys.stdin.readline())):
    dictionary.append(sys.stdin.readline().rstrip())

for i in range(26):
    new_text = ""
    for j in range(len(text)):
        new_text += alphabet[ord(text[j])-97]
    alphabet.append(alphabet.popleft())
    for j in dictionary:
        if j in new_text:
            print(new_text)
            break
