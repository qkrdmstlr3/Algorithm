"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/5622
"""
import sys

li, time = sys.stdin.readline(), 0
word = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
for i in range(len(li)-1):
    for j in range(8):
        if li[i] in word[j]:
            time += j + 3
print(time)
