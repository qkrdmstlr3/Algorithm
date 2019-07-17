"""
    Author : ParkEunsik
    Date   : 2019/07/17
    url    : https://www.acmicpc.net/problem/10845
"""
import sys


class queue(list):
    push = list.append

    def pop(self):
        if self.empty():
            return -1
        N = self[0]
        del self[0]
        return N

    def empty(self):
        if not self:
            return 1
        else:
            return 0

    def size(self):
        return len(self)

    def front(self):
        if self.empty():
            return -1
        return self[0]

    def back(self):
        if self.empty():
            return -1
        return self[-1]


q = queue()
for i in range(int(sys.stdin.readline())):
    ins = list(sys.stdin.readline().split())
    if ins[0] == 'push':
        q.push(ins[1])
    elif ins[0] == 'pop':
        print(q.pop())
    elif ins[0] == 'size':
        print(q.size())
    elif ins[0] == 'empty':
        print(q.empty())
    elif ins[0] == 'front':
        print(q.front())
    elif ins[0] == 'back':
        print(q.back())
