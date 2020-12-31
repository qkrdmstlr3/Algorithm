"""
    Author : ParkEunsik
    Date   : 2019/07/20
    url    : https://www.acmicpc.net/problem/11507
"""

import sys

card = sys.stdin.readline()
cnt = [13, 13, 13, 13]
check = []
i = 0
while i != len(card)-1:
    card_texture, card_num = card[i], ''.join(card[i+1:i+3])
    cr = [card_texture, card_num]  # 리스트로 묶어서 구별
    if cr in check:
        print("GRESKA")
        exit()
    else:
        check.append(cr)
    if card_texture == 'P':
        cnt[0] -= 1
    elif card_texture == 'K':
        cnt[1] -= 1
    elif card_texture == 'H':
        cnt[2] -= 1
    else:
        cnt[3] -= 1
    i += 3
for i in range(4):
    print(cnt[i], end=' ')
