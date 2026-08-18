from collections import deque

d = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9", 10:"a", 11:"b", 12:"c", 13:"d", 14:"e", 15:"f"}

def dec_to_hex(num):
    hexnum = deque()
    while num:
        hexnum.appendleft(d[num % 16])
        num //= 16
    return "".join(hexnum)

#testing
num = 5000
print(dec_to_hex(num))

