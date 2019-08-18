#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Time   : 2019/8/17 下午8:56
# Author : fred
menu = {
    '汽车': {
        '轿车': {
            '宝马': {
                '宝马760': {},
                '宝马M5': {},
                '宝马M3': {}
            },
            '奔驰': {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {},
            },
            '奥迪': {
                '奥迪A4L': {},
            },
        },
        '越野车': {
            '保时捷': {
                '保时捷Macan': {},
                '保时捷Cayenne': {},
            },
            '路虎': {},
            '英菲尼迪': {},
        },
        '卡车': {},
        '公交车': {},
    },
    '飞机': {
        '大飞机': {
            "大1": {
                '波音737': {}
            }
        },
        '小飞机': {
            '小1': {
                '湾流': {}
            }
        },
        '直升机': {},
    },
    '大炮': {}
}

layers = [menu, ]
while True:
    if len(layers) == 0:
        break
    current_layer = layers[-1]
    for key in current_layer:
        print(key)

    choice = input(">>:").strip()

    if choice == 'b':
        layers.pop(-1)
        continue
    if choice == 'q':
        break

    if choice not in current_layer:
        continue

    layers.append(current_layer[choice])
