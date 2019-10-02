"""
    Author : ParkEunsik
    Date   : 2019/10/02
    url    : https://www.acmicpc.net/problem/13413
"""

import sys

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    status1 = list(sys.stdin.readline().rstrip())
    status2 = list(sys.stdin.readline().rstrip())
    
    num1 = 0 #wb인 경우
    num2 = 0 #bw인 경우
    for i in range(n):
        if status1[i] == 'W' and status2[i] == 'B':
            num1 += 1
        elif status1[i] == 'B' and status2[i] == 'W':
            num2 += 1
    print(max(num1, num2))
