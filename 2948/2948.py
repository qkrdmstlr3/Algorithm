"""
    Author : ParkEunsik
    Date   : 2019/08/28
    url    : https://www.acmicpc.net/problem/2948
    correct percentage : 42.636%
"""

import sys
import datetime

D, M = map(int, sys.stdin.readline().split())
print(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'][datetime.date(2009, M, D).weekday()])
# datetime.date(2009, M, D).weekday() 로 요일의 숫자 반환
# datetime.datetime.today().weekday() 오늘 날짜
