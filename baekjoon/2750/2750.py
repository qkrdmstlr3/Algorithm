"""
    Author : ParkEunsik
    Date   : 2019/07/13
    url    : https://www.acmicpc.net/problem/2750
"""

li = []
for i in range(int(input())):
    li.append(int(input()))
li.sort()
for i in range(len(li)):
    print(li[i])
