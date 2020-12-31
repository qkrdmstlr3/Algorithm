"""
    Author : ParkEunsik
    Date   : 2019/07/23
    url    : https://www.acmicpc.net/problem/17294
"""

import sys

k, flag = list(sys.stdin.readline()), True

if len(k) > 3:
    for i in range(len(k)-3):
        if int(k[i]) - int(k[i+1]) != int(k[i+1]) - int(k[i+2]):
            flag = False
if flag:
    print("◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!")
else:
    print("흥칫뿡!! <(￣ ﹌ ￣)>")
