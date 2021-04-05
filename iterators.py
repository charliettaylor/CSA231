'''
An iterable is an object that has the property that allows it to be iterated
over, while an iterator is the object that actually has values within it
'''

from typing import Iterable


abc = 'abcdefg'.__iter__()
while True:
    try:
        print((abc.__next__()))
    except StopIteration:
        break


def group_n(iter: Iterable, n: int) -> list:
    group = iter.__iter__()
    groups = []
    grouping = []
    while True:
        try:
            element = str(group.__next__())
        except StopIteration:
            break
        grouping.append(element)
        if len(grouping) == 3:
            groups.append(grouping.copy())
            grouping.clear()
    return groups



class fib_range:
    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end
    
    def fib_list(self, start: int, end: int):
        fib = [1, 1]
        for i in range(1, end):
            fib.append(fib[i] + fib[i-1])
        return fib[start:end + 1]

    def __iter__(self):
        return self.fib_list(self.start, self.end).__iter__()

print(group_n('abcdefghijklmn',3))

fib = fib_range(2,6).__iter__()

while True:
    try:
        print((fib.__next__()))
    except StopIteration:
        break