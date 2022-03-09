#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = {'cat': 'кошка', 'dog': 'собака',
         'bird': 'птица', 'mouse': 'мышь'}
    print(a)
    print(a['cat'])
    print(a['bird'])
    a['elephant'] = 'бегемот'  # добавляем
    a['table'] = 'стол'  # добавляем
    print(a)
    a['elephant'] = 'слон'  # изменяем
    del a['table']  # удаляем
    print(a)
