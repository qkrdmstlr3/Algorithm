"""
    Author : ParkEunsik
    Date   : 2019/09/18
    url    : https://www.acmicpc.net/problem/1244
    correct percentage : 24.139%
"""

import sys

N = int(sys.stdin.readline())
switch = [True]+list(map(bool, list(map(int, sys.stdin.readline().split()))))

for _ in range(int(sys.stdin.readline())):
    gender, num = map(int, sys.stdin.readline().split())
    if gender == 1:
        for i in range(num, N+1, num):
            switch[i] = not switch[i]
    else:
        index = 1
        switch[num] = not switch[num]
        while num-index >= 1 and num+index <= N:
            if switch[num-index] == switch[num+index]:
                switch[num+index] = not switch[num+index]
                switch[num-index] = not switch[num-index]
            else:
                break
            index += 1
switch = list(map(int, switch))
for i in range(1, N+1):
    if i % 20 != 0:
        print(switch[i], end=' ')
    else:
        print(switch[i])
