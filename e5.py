#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = {x: x * x for x in (1, 2, 3, 4)}
    print(a)
    b = dict((x, x * x) for x in (1, 2, 3, 4))
    print(b)
    c = {name: len(name) for name in ('Stack', 'Overflow', 'Exchange') if
         len(name)
         > 6}
    print(c)
    d = dict((name, len(name)) for name in ('Stack', 'Overflow', 'Exchange') if
             len(name) > 6)
    print(d)
    initial_dict = {'x': 1, 'y': 2}
    e = {key: value for key, value in initial_dict.items() if key == 'x'}
    print(e)
    my_dict = {1: 'a', 2: 'b', 3: 'c'}
    swapped = dict(map(reversed, my_dict.items()))
    print(swapped)
    
