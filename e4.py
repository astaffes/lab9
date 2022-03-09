#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    nums = {1: 'one', 2: 'two', 3: 'three'}
    a = {'dog': 'собака', 'cat': 'кошка', 'mouse': 'мышь',
         'bird': 'птица', 'elephant': 'слон'}
    print(a)
    a.clear()
    print(a)
    nums2 = nums.copy()
    nums2[4] = 'four'
    print(nums)
    print(nums2)
    a = [1, 2, 3]
    c = dict.fromkeys(a)
    print(c)
    d = dict.fromkeys(a, 10)
    print(d)
    print(nums.get(1))
    print(nums.pop(1))
    print(nums)
    print(nums.popitem())
    print(nums)
    print(nums.setdefault(4, 'four'))
    print(nums)
    nums.update({6: 'six', 7: 'seven'})
    print(nums)
