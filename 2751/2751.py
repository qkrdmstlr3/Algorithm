"""
    Author : ParkEunsik
    Date   : 2019/07/16
    url    : https://www.acmicpc.net/problem/2751
"""

import sys


def merge_sort(li):
    if len(li) <= 1:
        return li
    center = len(li) // 2
    left = li[:center]
    right = li[center:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) != 0 and len(right) != 0:
            if left[0] > right[0]:
                result.append(right[0])
                right = right[1:]
            else:
                result.append(left[0])
                left = left[1:]
        elif len(left) != 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) != 0:
            result.append(right[0])
            right = right[1:]
    return result


li = []
for i in range(int(input())):
    li.append(int(sys.stdin.readline()))
li = merge_sort(li)
for i in range(len(li)):
    print(li[i])
