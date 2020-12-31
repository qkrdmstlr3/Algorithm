"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/10817
"""
time = list(map(int, input().split()))
h, m = time[0], time[1]

if m >= 45:
    print(h, m-45, sep=' ')
elif h == 0:
    print(23, m+15, sep=' ')
else:
    print(h-1, m+15,  sep=' ')
