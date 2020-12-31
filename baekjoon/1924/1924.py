"""
    Author : ParkEunsik
    Date   : 2019/07/10
    url    : https://www.acmicpc.net/problem/1924
"""

li = list(map(int, input().split()))
month, day, cnt = li[0], li[1], 0

max_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
dow = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i in range(0, month-1):
    cnt += max_day[i]
cnt += day
print(dow[cnt % 7])
