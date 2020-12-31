"""
    Author : ParkEunsik
    Date   : 2019/07/11
    url    : https://www.acmicpc.net/problem/1330
"""
num = list(map(int, input().split()))
if num[0] > num[1]:
    print('>')
elif num[0] == num[1]:
    print('==')
else:
    print('<')
