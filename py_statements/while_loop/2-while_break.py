#!/usr/bin/python3
x = 0
while x < 10:
    print('current value of x is;',x)
    print('now addin 1 to current value of x, x+1=', x+1)
    x += 1
    if x==4:
        print('x==4')
        print('Breaking coz x==4')
        break
    else:
        print('continueing....')
        continue
