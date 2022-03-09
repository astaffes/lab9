#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    dict1 = {'w': 1, 'x': 1}
    dict2 = {'x': 2, 'y': 2, 'z': 2}
    dict3 = {k: v for d in [dict1, dict2] for k, v in d.items()}
    print(dict3)
