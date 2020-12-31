"""
    Author : ParkEunsik
    Date   : 2019/09/04
    url    : https://www.acmicpc.net/problem/1213
    correct percentage : 36.197%
"""

import sys

name = list(sys.stdin.readline().rstrip())
alphabet = [0]*26
pelindrome = ""
count = 0  # 홀수인 알파벳의 숫자를 셈, 1개 까지만 가능
center = ""

for i in name:
    alphabet[ord(i)-65] += 1
for i in range(26):
    if alphabet[i] % 2 != 0:
        center += chr(i+65)
        count += 1
    pelindrome += chr(i+65)*(alphabet[i]//2)
if count > 1:
    print("I'm Sorry Hansoo")
else:
    print(pelindrome + center + ''.join(reversed(pelindrome)))
