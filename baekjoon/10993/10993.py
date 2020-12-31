"""
    Author : ParkEunsik
    Date   : 2019/07/08
    url    : https://www.acmicpc.net/problem/10993
    Correct percentage : 48.307%
"""
N = int(input())
li = ['*']
count = 1

while count != N:
    li2 = [None]*(2*len(li)+1)
    count += 1
    if count % 2 == 0:  # 짝수
        blanck_length = len(li[-1])-2
        for i in range(0, len(li2)):
            if i == 0:
                li2[i] = '*'*(len(li[-1])*2+3)
            elif i >= 1 and i <= len(li):
                li2[i] = ' '*i + '*' + ' '*(len(li)-i) + li[i-1] + ' '*(len(li)-i) + '*'
            elif i != len(li2)-1:
                li2[i] = ' '*i + '*' + ' '*blanck_length + '*'
                blanck_length -= 2
            else:
                li2[i] = ' '*i + '*'
            if count != N:
                li2[i] += ' '*i
    else:  # 홀수
        blanck_length = 1
        for i in range(0, len(li2)):
            if i == 0:
                li2[i] = ' '*(len(li2)-1) + '*'
            elif i < len(li):
                li2[i] = ' '*(len(li2)-1-i) + '*' + ' '*blanck_length + '*'
                blanck_length += 2
            elif i != len(li2)-1:
                li2[i] = ' '*(len(li2)-1-i) + '*'+ ' '*(i-len(li)) + li[i-len(li)] + ' '*(i-len(li)) + '*'
            else:
                li2[i] = '*'*(len(li[0])*2+3)
            if count != N:
                li2[i] += ' '*(len(li2)-1-i)
    li = li2

for i in range(len(li)):
    print(li[i])
