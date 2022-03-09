#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    nums = {1: 'one', 2: 'two', 3: 'three'}
    for i in nums:
        print(i)
    for i in nums:
        print(nums[i])
    n = nums.items()
    print(n)
    for key, value in nums.items():
        print(key, 'is', value)
    v_nums = []
    for v in nums.values():
        v_nums.append(v)
    print(v_nums)
    v_nums_2 = [v for v in nums.values()]
    print(v_nums_2)
