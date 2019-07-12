"""
    Author : ParkEunsik
    Date   : 2019/07/12
    url    : https://www.acmicpc.net/problem/10869
"""
num = list(map(int, input().split()))
print(num[0]+num[1], num[0]-num[1], num[0]*num[1], int(num[0]/num[1]), num[0] % num[1], sep='\n')
